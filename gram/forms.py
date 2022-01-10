from django import forms
from django.db.models import fields
from django.forms import ModelForm
from gram import models

from gram.models import Comments, Picture, Profile

class PictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = ('image','description')
        exclude = ('likes','comments')
        
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('username','bio','profile_pic')
        exclude = ('user',)

class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('comment',)