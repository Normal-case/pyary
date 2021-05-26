from django.db import models
from django.db.models.fields import related
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    nickname = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=11)
    profile_image = models.ImageField(upload_to='profile/%y/%m/%d', default='profile/profile_default.png')
    birth = models.DateField()

    def __str__(self):
        return self.nickname