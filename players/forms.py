from django import forms
from .models import Player
from .models import Contact


class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "country": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "role": forms.Select(attrs={
                "class": "form-select"
            }),

            "batting_style": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "bowling_style": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "matches": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "runs": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "wickets": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "biography": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5
            }),

            "image": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),
        }
        
class ContactForm(forms.ModelForm):

    class Meta:

        model = Contact

        fields = "__all__"