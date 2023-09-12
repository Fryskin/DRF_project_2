from django.conf import settings
from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='user')
    title = models.CharField(max_length=250, verbose_name='title')
    description = models.TextField(max_length=5000, verbose_name='description')
    preview = models.ImageField(upload_to='images/courses/', verbose_name='preview', **NULLABLE)

    def __str__(self):
        return f'Course({self.title})'

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'
        ordering = ('title',)


class Lesson(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='user')
    title = models.CharField(max_length=250, verbose_name='title')
    description = models.TextField(max_length=5000, verbose_name='description')
    preview = models.ImageField(upload_to='images/lessons/', verbose_name='preview', **NULLABLE)
    video_url = models.URLField(max_length=400, verbose_name='video_url')
    course = models.ManyToManyField('Course')

    def __str__(self):
        return f'Lesson({self.title})'

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'
        ordering = ('title',)


class Payment(models.Model):
    CASH = 'Cash'
    TRANSFER_TO_ACCOUNT = 'Transfer to account'
    PAYMENT_CHOICES = [
        (CASH, 'Cash'),
        (TRANSFER_TO_ACCOUNT, 'Transfer to account')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='user')
    date_of_payment = models.DateTimeField(verbose_name='date of payment')
    course_paid = models.ForeignKey(Course, verbose_name='course paid', on_delete=models.CASCADE, **NULLABLE)
    payment_amount = models.PositiveIntegerField(verbose_name='payment amount')
    type_of_payment = models.CharField(max_length=100, choices=PAYMENT_CHOICES, verbose_name='type of payment')

    def __str__(self):
        return f'Payment({self.type_of_payment})'

    class Meta:
        verbose_name = 'payment'
        verbose_name_plural = 'payments'
        ordering = ('user',)


class Subscription(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='course')
    is_active = models.BooleanField(default=False, verbose_name='is active')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='user')

    def __str__(self):
        return f'Subscription({self.is_active})'

    class Meta:
        verbose_name = 'subscription'
        verbose_name_plural = 'subscriptions'
        ordering = ('course',)
