# Generated by Django 3.0.4 on 2020-04-26 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20200426_1148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image_post',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='thread',
            old_name='image_thread',
            new_name='image',
        ),
    ]
