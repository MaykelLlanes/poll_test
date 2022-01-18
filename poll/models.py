from django.db import models
from django.forms import ModelForm
from model_utils import Choices


# Create your models here.

class Person(models.Model):
    SEX_CHOICES = Choices('M','F')

    name = models.CharField(max_length=250)
    age = models.IntegerField(blank=True)    
    sex = models.CharField(choices=SEX_CHOICES, default=SEX_CHOICES.M, max_length=1)
    personal_information = models.TextField(max_length=500, blank=True)
    education_level = models.CharField(max_length=150, blank=True)
    body_weight = models.FloatField()

    def __str__(self):
        return self.name