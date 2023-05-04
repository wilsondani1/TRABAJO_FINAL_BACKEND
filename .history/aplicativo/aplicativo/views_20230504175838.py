from django.shortcuts import render
from django.core.mail import EmailMessage

from django.template.loader import render_to_string

def send_email(mail):
    context = {'mail' : mail}

    template = get_template('correo.html')
    content = template.render()

def index(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')

        send_email()

    return render(request, 'index.html', {})
