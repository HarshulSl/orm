# Generated by Django 5.1.2 on 2024-10-22 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bank',
            fields=[
                ('Name', models.CharField(max_length=10)),
                ('Accno', models.IntegerField(primary_key='Accno', serialize=False)),
                ('Amount', models.FloatField()),
                ('interest', models.FloatField()),
                ('duedate', models.DateField()),
            ],
        ),
    ]
