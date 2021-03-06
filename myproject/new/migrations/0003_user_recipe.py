# Generated by Django 3.0.8 on 2020-08-11 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0002_ingredient_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('ingredients', models.CharField(max_length=512)),
                ('description', models.CharField(max_length=512)),
                ('steps', models.CharField(max_length=4096)),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
    ]
