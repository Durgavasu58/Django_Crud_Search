# Generated by Django 3.2.5 on 2021-07-15 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(max_length=20)),
                ('dob', models.DateField(max_length=8)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
