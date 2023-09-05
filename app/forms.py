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
            attrs={
                'placeholder': 'Имя',
                'class': 'form-control'}
        )
    )
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Телефон',
                'class': 'form-control'}
        )
    )
    city = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Выберите город',
                'class': 'form-control'}
        )
    )
    usluga = forms.ChoiceField(
        choices=services_list,
        widget=forms.Select(
            attrs={
                'class': 'form-select'}
        )
    )



class CallmebackForm(forms.Form):
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Телефон',
                'class': 'form-control'}
        )
    )
