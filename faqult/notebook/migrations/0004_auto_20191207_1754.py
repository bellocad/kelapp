# Generated by Django 3.0 on 2019-12-07 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0003_auto_20191207_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='bagian',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='notebook.bagian', verbose_name='Bagian'),
        ),
    ]
