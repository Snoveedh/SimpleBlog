# Generated by Django 3.1.6 on 2021-10-14 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysimpleblog', '0010_post_snippets'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='snippets',
            new_name='snippet',
        ),
    ]
