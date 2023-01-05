#Import from the core django
from django import forms
#Import from local app/library
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from testimonial.models import Testimonial


class LoginForm(forms.ModelForm):
      class Meta:
        model= User
        fields=  ['email' ,'password'  ] 

class TestimonialForm(forms.ModelForm):
    class Meta:
        model= Testimonial
        fields= '__all__'

