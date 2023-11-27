from django.db import models
from user.models import *

# Create your models here.
class Todo(models.Model):
    user =models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    todo = models.CharField(max_length=150)

    def __str__(self):
        return self.todo