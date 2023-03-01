from django.forms import ModelForm, TextInput, Textarea
from .models import Requests


class ContactForm(ModelForm):
    class Meta:
        model = Requests
        fields = ['name_customer', 'phone_number', 'text_request']
        widgets = {"name_customer": TextInput(attrs={"class": "modal-input", "placeholder": "Введите Ваше имя"}),
                   "phone_number": TextInput(attrs={"class": "modal-input", "placeholder": "Введите номер телефона"}),
                   "text_request": Textarea(attrs={"class": "modal-input-area", "placeholder": "Ваш комментарий"})}

