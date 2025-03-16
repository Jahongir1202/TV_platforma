from django import forms
from .models import Ariza,TestQuestion

class ArizaForm(forms.ModelForm):
    class Meta:
        model = Ariza
        fields = ["full_name", "phone_number", "message"]
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Ismingizni kiriting", "class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"placeholder": "Telefon raqamingiz", "class": "form-control"}),
            "message": forms.Textarea(attrs={"placeholder": "Xabaringizni kiriting", "class": "form-control", "rows": 4}),
        }
class TestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop("questions", [])
        super().__init__(*args, **kwargs)

        for question in questions:
            choices = [
                (1, question.option1),
                (2, question.option2),
                (3, question.option3),
                (4, question.option4),
            ]
            self.fields[f"question_{question.id}"] = forms.ChoiceField(
                choices=choices, widget=forms.RadioSelect, label=question.question_text, required=True
            )