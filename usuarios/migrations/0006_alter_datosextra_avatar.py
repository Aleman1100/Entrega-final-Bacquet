# Generated by Django 4.2.6 on 2023-11-18 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_datosextra_biografia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosextra',
            name='avatar',
            field=models.ImageField(null=True, upload_to='avatares'),
        ),
    ]
