# Generated by Django 3.2.23 on 2023-12-17 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_receipe_receipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipe',
            name='receipe_image',
            field=models.ImageField(storage='media/receipe', upload_to='receipe'),
        ),
    ]
