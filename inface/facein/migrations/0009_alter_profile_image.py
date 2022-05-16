# Generated by Django 4.0.3 on 2022-05-16 14:58

from django.db import migrations, models
import facein.models


class Migration(migrations.Migration):

    dependencies = [
        ('facein', '0008_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=facein.models.path_and_rename),
        ),
    ]
