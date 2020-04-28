# Generated by Django 3.0.4 on 2020-04-27 09:33

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_post_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='answer',
        ),
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default=None, force_format=None, keep_meta=True, null=True, quality=0, size=[400, 250], upload_to='media/'),
        ),
    ]
