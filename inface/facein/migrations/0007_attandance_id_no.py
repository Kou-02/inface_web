# Generated by Django 4.0.3 on 2022-05-21 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facein', '0006_std_details_no_of_classes'),
    ]

    operations = [
        migrations.AddField(
            model_name='attandance',
            name='id_no',
            field=models.CharField(blank=True, default='', max_length=70, null=True),
        ),
    ]