from django import forms
from .models import NamaHewan as NamaHewanModel


class inputbinatang(forms.ModelForm):
    class Meta :
        model = NamaHewanModel
        fields = ('nama_hewan', 'species', 'hewan', 'umur')