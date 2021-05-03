from django.forms import ModelForm
from .models import Itanikom

class ItanikomForm(ModelForm):
    class Meta:
        model = Itanikom
        fields = ['title', 'memoItanikom', 'memoEnglish', 'important']
