# Generated by Django 3.0.4 on 2020-04-25 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20200425_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testmodel',
            name='describe',
        ),
    ]
