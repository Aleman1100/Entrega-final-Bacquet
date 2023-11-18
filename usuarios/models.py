from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class DatosExtra(models.Model):
    user = models.OneToOneField(User, related_name='datosextra', on_delete=models.CASCADE)
    biografia = RichTextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)