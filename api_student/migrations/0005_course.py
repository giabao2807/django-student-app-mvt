# Generated by Django 3.2.8 on 2022-05-13 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_student', '0004_department_student_email_student_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=256)),
                ('limit', models.IntegerField(default=30)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('students', models.ManyToManyField(blank=True, null=True, to='api_student.Student')),
            ],
        ),
    ]
