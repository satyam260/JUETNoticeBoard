# Generated by Django 2.1 on 2019-03-22 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190322_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticeboard',
            name='url',
        ),
    ]