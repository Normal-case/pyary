from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View, DetailView, CreateView
from django.contrib.auth.models import User
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile

class ProfileMain(View):
    def get(self, request, id):
        target_user = self.request.user
        return render(request, 'profileapp/main.html', {'target_user':target_user})

class ProfileCreate(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    template_name = 'profileapp/create.html'
    form_class = ProfileCreationForm

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profileapp:main', kwargs={'id': self.object.user.username})