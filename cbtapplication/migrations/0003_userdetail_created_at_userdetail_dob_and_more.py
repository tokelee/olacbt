# Generated by Django 5.1.3 on 2024-11-25 11:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbtapplication', '0002_alter_question_diagram_alter_userdetail_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='dob',
            field=models.DateField(blank=True, default=datetime.datetime(2006, 1, 1, 0, 0), verbose_name='Date of birth'),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='is_computer_literate',
            field=models.BooleanField(default=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='examsubject',
            name='department',
            field=models.CharField(choices=[('all', 'All Departments'), ('science', 'Science'), ('business', 'Business'), ('humanity', 'Humanity')], max_length=50),
        ),
        migrations.AlterField(
            model_name='question',
            name='diagram',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='class_year',
            field=models.CharField(blank=True, choices=[('1', 'SS1'), ('2', 'SS2'), ('3', 'SS3')], max_length=5),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='department',
            field=models.CharField(blank=True, choices=[('science', 'Science'), ('business', 'Business'), ('humanity', 'Humanity')], max_length=50),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='role',
            field=models.CharField(choices=[('student', 'Student'), ('moderator', 'Moderator')], default='student', max_length=20),
        ),
    ]
