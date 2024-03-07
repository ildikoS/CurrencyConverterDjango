from django.db import models
from django import forms

# Create your models here.
# Run py manage.py makemigrations when there is any change
# py manage.py migrate
class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length = 254)

class Currency(forms.Form):
    base_curr = forms.CharField(label="base_curr", required=False)
    curr_to = forms.CharField(label="curr_to", required=False)
    amount = forms.IntegerField(required=False)