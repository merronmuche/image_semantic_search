# Generated by Django 4.2.1 on 2023-07-05 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_image_name_image_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='name',
            new_name='image',
        ),
    ]