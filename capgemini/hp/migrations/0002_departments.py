# Generated by Django 2.2.7 on 2019-11-26 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptid', models.CharField(max_length=10)),
                ('deptname', models.CharField(max_length=50)),
            ],
        ),
    ]