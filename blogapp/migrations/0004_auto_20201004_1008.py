# Generated by Django 3.1.2 on 2020-10-04 10:08

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_auto_20201004_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
