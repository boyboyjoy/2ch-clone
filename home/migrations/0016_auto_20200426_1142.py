# Generated by Django 3.0.4 on 2020-04-26 11:42

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20200426_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=0, size=[400, 250], upload_to='media/'),
        ),
    ]
