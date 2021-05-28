from django.shortcuts import render
from django.views.generic import View, CreateView
from django.utils.safestring import mark_safe
from datetime import datetime
from django.urls import reverse
import cv2

from django.views.generic.detail import DetailView
from .calendar import Calendar
from .models import Diary
from .forms import DiaryCreationForm
from .change_image_name import file_path_decode
from memory_storage import settings
import easyocr

# Create your views here.
class HomeView(View):
    def get(self, request, id):
        now = datetime.now()
        cal = Calendar(now.year, now.month, self.request.user)
        html_cal = cal.formatmonth(withyear=True)
        result_cal = mark_safe(html_cal)
        return render(request, 'diaryapp/home.html', {'calendar':result_cal})


class DiaryCreate(CreateView):
    model = Diary
    context_object_name = 'target_diary'
    template_name = 'diaryapp/create.html'
    form_class = DiaryCreationForm

    def form_valid(self, form):
        temp_diary = form.save(commit=False)
        temp_diary.user = self.request.user
        temp_diary.save()

        if temp_diary.ocr_image:
            reader = easyocr.Reader(['ko'], gpu=True)
            path = settings.MEDIA_ROOT + '/' + temp_diary.ocr_image.name
            img = file_path_decode(path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            result = reader.readtext(gray)

            text_list = list()
            for word in result:
                text_list.append(word[1])
            
            temp_diary.content = ' '.join(text_list)
            temp_diary.save()
        
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('diaryapp:read', kwargs={'pk':self.object.pk})

class DiaryRead(DetailView):
    model = Diary
    context_object_name = 'target_diary'
    template_name = 'diaryapp/detail.html'