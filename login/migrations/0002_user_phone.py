# Generated by Django 3.2.2 on 2021-05-10 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=9999999999, max_length=10),
            preserve_default=False,
        ),
    ]
