from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = [
            "first_name",
            "last_name",
            "email",
            "classe",
            "phone",
            "birth_date",
            "active",
        ]

        widgets = {
            "birth_date": forms.DateInput(
                attrs={"type": "date"},
                format="%Y-%m-%d"
            ),
        }

    def clean_phone(self):
        phone = self.cleaned_data["phone"].replace(" ", "")

        if phone and (
            len(phone) != 9
            or not phone.isascii()
            or not phone.isdigit()
        ):
            raise forms.ValidationError(
                "Le numéro doit contenir 9 chiffres, par exemple 77 123 45 67."
            )

        return phone