# Generated by Django 4.1.7 on 2023-07-16 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_list', '0002_alter_master_courses_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master_courses',
            name='course_name',
            field=models.TextField(),
        ),
    ]
