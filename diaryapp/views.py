from django.shortcuts import render
from django.views.generic import View
from django.utils.safestring import mark_safe
from datetime import datetime
import calendar
from .calendar import Calendar

# Create your views here.
class HomeView(View):
    def get(self, request):
        now = datetime.now()
        cal = Calendar(now.year, now.month)
        html_cal = cal.formatmonth(withyear=True)
        result_cal = mark_safe(html_cal)
        return render(request, 'diaryapp/home.html', {'calendar':result_cal})


class DiaryCreate(View):
    def get(self, request):
        return render(request, 'diaryapp/create.html')