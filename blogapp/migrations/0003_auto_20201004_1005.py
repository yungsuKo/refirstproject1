# Generated by Django 3.1.2 on 2020-10-04 10:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20201004_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
