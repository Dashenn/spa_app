from django import forms
from django.core.validators import RegexValidator
from .models import Service

phone_validator = RegexValidator(
    regex=r"^(\+7|8)\d{10}$",
    message="Введите номер в формате +7XXXXXXXXXX или 8XXXXXXXXXX",
)

class RequestForm(forms.Form):
    first_name = forms.CharField(
        label="Имя",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control rounded"}),
    )
    last_name = forms.CharField(
        label="Фамилия",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control rounded"}),
    )
    phone_number = forms.CharField(
        label="Телефон",
        max_length=12,
        validators=[phone_validator],
        widget=forms.TextInput(attrs={"class": "form-control rounded"}),
    )
    desired_service = forms.ChoiceField(
        label="Желаемая услуга",
        choices=[],
        widget=forms.Select(attrs={"class": "form-control rounded"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        services = Service.objects.all()
        self.fields["desired_service"].choices = [(s.id, s.name) for s in services]
