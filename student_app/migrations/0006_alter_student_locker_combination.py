# Generated by Django 4.2.7 on 2023-11-27 00:25

from django.db import migrations, models
import student_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0005_alter_student_locker_combination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='locker_combination',
            field=models.CharField(default='12-12-12', validators=[student_app.validators.validate_locker_combination]),
        ),
    ]
