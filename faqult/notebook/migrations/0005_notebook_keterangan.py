# Generated by Django 3.0 on 2019-12-07 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0004_auto_20191207_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebook',
            name='keterangan',
            field=models.BooleanField(default=False, verbose_name='Keterangan'),
        ),
    ]
