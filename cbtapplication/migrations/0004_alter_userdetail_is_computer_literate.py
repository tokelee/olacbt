# Generated by Django 5.1.3 on 2024-11-26 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbtapplication', '0003_userdetail_created_at_userdetail_dob_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='is_computer_literate',
            field=models.BooleanField(default=False, max_length=10, verbose_name='I am computer literate'),
        ),
    ]