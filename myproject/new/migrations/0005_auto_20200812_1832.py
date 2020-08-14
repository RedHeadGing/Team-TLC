# Generated by Django 3.0.8 on 2020-08-12 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0004_user_recipe_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_recipe',
            name='description',
            field=models.TextField(max_length=512),
        ),
        migrations.AlterField(
            model_name='user_recipe',
            name='ingredients',
            field=models.TextField(max_length=512),
        ),
        migrations.AlterField(
            model_name='user_recipe',
            name='steps',
            field=models.TextField(max_length=4096),
        ),
    ]