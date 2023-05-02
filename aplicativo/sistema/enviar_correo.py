from django.conf import settings
from django.core.mail import EmailMultiAlternatives

def send_user_mail(user):
    subject = 'Correo desde django'
    template = get_template('templates/mi_template_correo.html')

    content = template.render({
        'user': user,
    })

    message = EmailMultiAlternatives(subject,
                                    settings.EMAIL_HOST_USER, #Remitente
                                    [user.email]) #Destinatario

    message.attach_alternative(content, 'text/html')
    message.send()