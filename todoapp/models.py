from django.db import models
from user.models import *
from autoslug import AutoSlugField
from django.urls import reverse

# Create your models here.
class Todo(models.Model):
    user =models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    todo = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from ='todo')

    def __str__(self):
        return self.todo
    
    def get_absolute_url(self):
        return reverse("todo-detay", kwargs={"slug": self.slug})
    