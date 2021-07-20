# Generated by Django 3.1.7 on 2021-04-24 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sikept', '0010_auto_20210424_1341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dokumen',
            old_name='description',
            new_name='nama_pejabat',
        ),
        migrations.AddField(
            model_name='dokumen',
            name='tanggal_surat',
            field=models.DateField(null=True, verbose_name='Tanggal Surat'),
        ),
        migrations.AlterField(
            model_name='dokumen',
            name='category',
            field=models.CharField(choices=[('SK Pendirian', 'SK Pendirian'), ('SK Perubahan', 'SK Perubahan'), ('SK Penutupan', 'SK Penutupan'), ('SK Pembukaan', 'SK Pembukaan'), ('SK Penyesuaian Nomenklatur', 'SK Penyesuaian Nomenklatur'), ('Akta Pendirian', 'Akta Pendirian'), ('Akta Perubahan', 'Akta Perubahan'), ('SK Menkumham', 'SK Menkumham'), ('Pencatatan SK Menkumham', 'Pencatatan SK Menkumham'), ('Rekomendasi', 'Rekomendasi'), ('Rekomendasi Akreditasi', 'Rekomendasi Akreditasi'), ('Surat Permohonan', 'Surat Permohonan')], max_length=200, null=True),
        ),
    ]