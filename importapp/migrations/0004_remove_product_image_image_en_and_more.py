# Generated by Django 4.1.1 on 2023-03-29 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('importapp', '0003_alter_product_image_options_product_image_image_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_image',
            name='Image_en',
        ),
        migrations.RemoveField(
            model_name='product_image',
            name='Image_ru',
        ),
        migrations.RemoveField(
            model_name='product_image',
            name='Image_uz',
        ),
    ]
