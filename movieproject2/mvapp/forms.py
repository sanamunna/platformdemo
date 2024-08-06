from django import forms
from .models import Movie
class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['image','description','release_date','actors','trailer_link']