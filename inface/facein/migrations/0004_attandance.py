# Generated by Django 4.0.3 on 2022-05-21 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facein', '0003_rename_id_no_profile_id_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='attandance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff', models.CharField(default='none', max_length=70)),
                ('subject', models.CharField(default='library', max_length=70)),
                ('section', models.CharField(default='A', max_length=20)),
                ('department', models.CharField(default='Ph.D', max_length=70)),
                ('student', models.CharField(default='', max_length=70)),
            ],
        ),
    ]