# Generated by Django 2.2.7 on 2019-11-26 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hp', '0002_departments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manid', models.CharField(max_length=10)),
                ('manname', models.CharField(max_length=50)),
            ],
        ),
    ]
