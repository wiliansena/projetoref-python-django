from django import forms

from .models import Ref, Color

class refForm(forms.ModelForm):

    class Meta:
        model = Ref
        fields = ('reference','description', 'color_text', 'status')

class colorForm(forms.ModelForm):

    class Meta:
        model = Color
        fields = ('color_text',)