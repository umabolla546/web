# Generated by Django 3.1 on 2023-08-08 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Boogging_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
