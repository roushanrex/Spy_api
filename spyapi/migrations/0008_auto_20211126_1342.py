# Generated by Django 3.2.9 on 2021-11-26 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spyapi', '0007_activated_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhonedataPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devicename', models.CharField(max_length=255)),
                ('simname', models.CharField(max_length=255)),
                ('latitude', models.CharField(max_length=255)),
                ('longitude', models.CharField(max_length=255)),
                ('phonenumber', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='activated',
            name='phonenumber',
        ),
    ]
