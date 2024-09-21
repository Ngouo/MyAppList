from django.db import models

# Create your models here.


class Task(models.Model):
  tache = models.CharField(max_length=5000)
  
  def __str__(self):
    return self.tache