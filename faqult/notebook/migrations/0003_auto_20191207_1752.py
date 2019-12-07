# Generated by Django 3.0 on 2019-12-07 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0002_auto_20191205_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='catatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catatan', models.TextField(max_length=300, null=True, verbose_name='Catatan')),
                ('kategori', models.CharField(max_length=100, null=True, verbose_name='Kategori')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
        ),
        migrations.RemoveField(
            model_name='notebook',
            name='sub_bagian',
        ),
        migrations.AddField(
            model_name='notebook',
            name='prioritas',
            field=models.CharField(max_length=100, null=True, verbose_name='Prioritas'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='bagian',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='notebook.bagian', verbose_name='Sub Bagian'),
        ),
    ]
