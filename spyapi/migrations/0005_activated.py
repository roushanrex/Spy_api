# Generated by Django 3.2.9 on 2021-11-26 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spyapi', '0004_auto_20211125_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', models.IntegerField()),
            ],
        ),
    ]
