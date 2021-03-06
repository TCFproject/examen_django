# Generated by Django 4.0 on 2021-12-10 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address_street', models.CharField(max_length=100)),
                ('address_number', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=20)),
                ('postcode', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('picture', models.CharField(max_length=200)),
            ],
        ),
    ]
