# Generated by Django 5.0 on 2023-12-05 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_alter_menu_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(default='', upload_to='static/menu_images/'),
        ),
    ]
