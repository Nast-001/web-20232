# Generated by Django 4.2.1 on 2023-05-24 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailingList', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailinglist',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
