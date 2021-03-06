# Generated by Django 3.0 on 2019-12-05 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=125)),
                ('profesi', models.CharField(blank=True, max_length=125, null=True)),
                ('no_telp', models.CharField(max_length=125)),
                ('pertanyaan', models.CharField(max_length=125)),
                ('kategori', models.CharField(max_length=125)),
                ('bagian', models.CharField(max_length=125)),
                ('sub_bagian', models.CharField(max_length=125)),
                ('jawaban', models.CharField(max_length=125)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'notebook',
                'verbose_name_plural': 'notebooks',
                'ordering': ['nama', 'kategori'],
            },
        ),
    ]
