from django import forms
from .models.character import Character

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['player_name','name', 'initiative', 'groups']