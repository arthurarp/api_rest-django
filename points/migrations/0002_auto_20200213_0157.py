# Generated by Django 2.2.10 on 2020-02-13 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='points',
            name='approve',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='points',
            name='description',
            field=models.TextField(default=None),
        ),
    ]