# Generated by Django 5.0.3 on 2024-03-23 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0003_alter_dog_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='photo',
            field=models.ImageField(null=True, upload_to='dogs'),
        ),
    ]
