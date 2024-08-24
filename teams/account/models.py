from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('user_detail', args=[str(self.id)])