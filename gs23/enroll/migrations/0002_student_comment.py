# Generated by Django 4.2.1 on 2023-06-21 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='comment',
            field=models.CharField(default='not available', max_length=40),
        ),
    ]
