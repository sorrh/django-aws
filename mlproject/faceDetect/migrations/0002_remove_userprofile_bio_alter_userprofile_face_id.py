# Generated by Django 4.1.1 on 2022-10-11 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faceDetect', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='face_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
