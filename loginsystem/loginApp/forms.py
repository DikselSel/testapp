from django.forms import ModelForm, widgets
from .models import *

class NapiszForm(ModelForm):
    class Meta:
        model = Napisz
        fields = '__all__'
        #widgets = {
           #widgets 'tytul': forms.TextInput(attrs={'class': 'text input'}),
           # 'wykonanie': forms.TextInput(attrs={'class': 'text input'}),
        #}
        