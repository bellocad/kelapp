# Generated by Django 3.1.7 on 2021-04-14 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sikept', '0003_auto_20210414_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='dokumen',
            name='tags',
            field=models.ManyToManyField(to='sikept.Tag'),
        ),
    ]
