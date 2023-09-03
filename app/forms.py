from django import forms
from django.conf import settings
from django.core.mail import send_mail


class ContactForm(forms.Form):
    services_list = [
        ('Ремонт скважин', 'Ремонт скважин'),
        ('Очистка скважин', 'Очистка скважин'),
        ('Замена насоса', 'Замена насоса')
    ]
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Имя'})
    )
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(
            attrs={'placeholder': 'Телефон'})
    )
    city = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={'placeholder': 'Выберите город'})
    )
    usluga = forms.ChoiceField(
        choices=services_list
    )
