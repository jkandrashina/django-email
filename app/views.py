from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect

from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            city = form.cleaned_data['city']
            usluga = form.cleaned_data['usluga']
            
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

            return redirect('email_sent')
    else:
        form = ContactForm()
        return render(request, 'app/index.html', {'form': form})


def email_sent(request):
    return render(request, 'app/email_sent.html')
