# Generated by Django 3.1.6 on 2021-08-06 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysimpleblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Mysimple Blog!', max_length=255),
        ),
    ]
