# Generated by Django 5.0.1 on 2024-05-06 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_userdata_course_userdata_school_alter_userdata_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='dislikes',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='likes',
            field=models.TextField(default='', max_length=500),
        ),
    ]
