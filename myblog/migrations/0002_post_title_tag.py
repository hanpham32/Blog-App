# Generated by Django 3.2.5 on 2021-08-11 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='', max_length=255),
        ),
    ]
