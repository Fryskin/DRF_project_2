# Generated by Django 4.2.3 on 2023-09-12 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_subscription'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'ordering': ('course',), 'verbose_name': 'subscription', 'verbose_name_plural': 'subscriptions'},
        ),
    ]
