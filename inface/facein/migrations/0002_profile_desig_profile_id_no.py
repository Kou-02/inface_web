# Generated by Django 4.0.3 on 2022-05-14 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facein', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='desig',
            field=models.TextField(default='0'),
        ),
        migrations.AddField(
            model_name='profile',
            name='id_no',
            field=models.TextField(default='0'),
        ),
    ]
