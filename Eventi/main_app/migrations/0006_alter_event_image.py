# Generated by Django 5.1.4 on 2025-01-21 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(default='', upload_to='main_app/static/uploads/'),
        ),
    ]
