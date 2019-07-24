from django import forms
from .models import Mentor, Mentee, Blog

class inputmentor(forms.ModelForm):
    class Meta :
        model = Mentor
        fields = ('id','nama', 'pengalaman', 'motto', 'photo')

class inputmentee(forms.ModelForm):
    class Meta :
        model = Mentee
        fields = ('id','nama', 'motto', 'photo')

class inputblog(forms.ModelForm):
    class Meta :
        model = Blog
        fields = ('title', 'content', 'date_create', 'photo')