# Generated by Django 2.0.6 on 2018-06-18 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_Library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Existing_User_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=25)),
                ('movie_id', models.CharField(max_length=25)),
                ('user_rating', models.CharField(max_length=10)),
            ],
        ),
    ]
