# Generated by Django 4.2.6 on 2023-11-18 01:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_remove_datosextra_biografia'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosextra',
            name='biografia',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]