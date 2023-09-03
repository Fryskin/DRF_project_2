from django.db import models

from users.models import NULLABLE


class Course(models.Model):
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
    title = models.CharField(max_length=250, verbose_name='title')
    description = models.TextField(max_length=5000, verbose_name='description')
    preview = models.ImageField(upload_to='images/lessons/', verbose_name='preview', **NULLABLE)
    video_url = models.URLField(max_length=400, verbose_name='video_url')

    def __str__(self):
        return f'Lesson({self.title})'

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'
        ordering = ('title',)




