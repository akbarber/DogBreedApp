from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User, Group
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib import admin
from django.core.validators import *

import base64
# Create your models here.



class Breed(models.Model):
    SIZE = (
        ('Tiny', 'Tiny'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    )
# subclasses at end if i want to try IntegerChoices    

    name = models.CharField(max_length=50, unique=True, blank=False)
    size = models.CharField(max_length=6, choices=SIZE) 
    friendliness = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    trainability = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    sheddingamount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    exerciseneeds = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return str(self.name)

# class BreedAdmin(admin.ModelAdmin):
#     list_display = ('name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds')


class Dog(models.Model):
    GENDER = (
        ('Female', 'Female'),
        ('Male', 'Male'),
    )
    name = models.CharField(max_length=50, blank=False)
    age = models.PositiveIntegerField()
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE) #related_name='breedinfo'
    gender = models.CharField(max_length=10, blank=False, choices=GENDER)
    color = models.CharField(max_length=25, blank=False)
    favoritefood = models.CharField(max_length=50, blank=False)
    favoritetoy = models.CharField(max_length=50, blank=False)
 
        
    def __str__(self):
        return str(self.name)

# class DogAdmin(admin.ModelAdmin):
#     list_display = ('name', 'age', 'gender', 'color', 'favoritefood', 'favoritetoy', 'breed')           
