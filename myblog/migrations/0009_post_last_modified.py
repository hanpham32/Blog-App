# Generated by Django 3.2.7 on 2021-10-02 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0008_auto_20211002_0549'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]