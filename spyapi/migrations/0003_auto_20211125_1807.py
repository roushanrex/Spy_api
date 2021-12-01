# Generated by Django 3.2.9 on 2021-11-25 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spyapi', '0002_auto_20211125_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phonenumber', models.IntegerField(max_length=12)),
                ('password', models.CharField(max_length=255)),
                ('coupon', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Food',
        ),
    ]