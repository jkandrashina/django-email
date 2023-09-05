from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect

from .forms import ContactForm, CallmebackForm


def contact_view(request):
    if request.method == 'POST':
        if 'contact-form' in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                name = contact_form.cleaned_data['name']
                phone = contact_form.cleaned_data['phone']
                city = contact_form.cleaned_data['city']
                usluga = contact_form.cleaned_data['usluga']
            
                msg = f'Отправитель: {name}\n'
                msg += f'Номер телефона: {phone}\n'
                msg += f'Город: {city}\n'
                msg += f'Интересует услуга: {usluga}'
            
                send_mail(
                    subject=usluga,
                    message=msg,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.RECIPIENT_ADDRESS]
                )
        elif 'callmeback-form' in request.POST:
            callme_form = CallmebackForm(request.POST)
            if callme_form.is_valid():
                phone = callme_form.cleaned_data['phone']
                subj = 'ochistka-skvajin.ru: запрос обратного звонка'
                
                msg = f'Сообщение с сайта ochistka-skvajin.ru\nПользователь запросил обратный звонок'
                msg += f'\n\nНомер телефона: {phone}\n'
            
                send_mail(
                    subject=subj,
                    message=msg,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.RECIPIENT_ADDRESS]
                )

        return redirect('email_sent')
    else:
        contact_form = ContactForm()
        callme_form = CallmebackForm()
        return render(
            request,
            'app/index.html',
            {'contact_form': contact_form, 'callme_form': callme_form})


def email_sent(request):
    return render(request, 'app/email_sent.html')
