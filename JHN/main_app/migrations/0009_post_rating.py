# Generated by Django 4.2.1 on 2023-06-06 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_delete_post1_delete_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.IntegerField(default=5),
        ),
    ]
