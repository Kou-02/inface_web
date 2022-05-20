# Generated by Django 4.0.3 on 2022-05-19 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facein', '0009_alter_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classa', models.CharField(default='student', max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='department',
            new_name='Department',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='desig',
            new_name='Designation',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='id_no',
            new_name='ID_no',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='Profile_picture',
        ),
    ]
