# Generated by Django 2.1.5 on 2020-01-06 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=5)),
                ('age', models.DateField()),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]
