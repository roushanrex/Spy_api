# Generated by Django 3.2.9 on 2021-11-26 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spyapi', '0010_phonedata_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonedata',
            name='deviceid',
            field=models.CharField(default=12, max_length=255),
            preserve_default=False,
        ),
    ]
