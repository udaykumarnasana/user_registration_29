from django import forms

from app.models import *

class userform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']



class profileform(forms.ModelForm):
    class Meta:
        model=profile
        fields=['address','profile_pic']
    