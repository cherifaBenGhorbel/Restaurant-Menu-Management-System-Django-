from django import forms
from menu.models import Menu

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = "__all__"
    