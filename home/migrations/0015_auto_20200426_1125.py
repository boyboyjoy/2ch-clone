# Generated by Django 3.0.4 on 2020-04-26 11:25

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20200426_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=0, size=[500, 300], upload_to='media/'),
        ),
    ]