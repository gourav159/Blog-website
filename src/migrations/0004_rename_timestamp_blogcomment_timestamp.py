# Generated by Django 4.0.2 on 2022-02-17 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0003_blogcomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcomment',
            old_name='timestamp',
            new_name='timeStamp',
        ),
    ]
