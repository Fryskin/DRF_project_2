from datetime import datetime

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from users.models import User


@shared_task
def update_of_course_mailing(model):
    if model == 'User':
        for user in User.objects.all():
            e_mail = user.email
            message_title = 'The new course update...'
            message_content = "The new course update is waiting for you!" \
                              "Let's sign in and check new updates for you."
            send_mail(
                subject=message_title,
                message=message_content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[e_mail]
            )


@shared_task
def drop_out_non_active_student():
    datetime_now = datetime.now()
    for user in User.objects.all():
        last_login = user.last_login
        duration = datetime_now - last_login
        duration_in_days = duration.days
        if duration_in_days > 28:
            user.is_active = False


