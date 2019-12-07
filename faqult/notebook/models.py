from django.db import models

# datatable bagian
class bagian(models.Model):

    nama_bagian = models.CharField(max_length=100)
    sub_bagian = models.CharField(max_length=100,null=True,blank=True)

    created = models.DateTimeField(verbose_name=('Created'),auto_now_add=True)
    updated = models.DateTimeField(verbose_name=('Updated'),auto_now=True)


    class Meta:
        verbose_name = ('Bagian')
        verbose_name_plural = ('Bagian')
        ordering = ['nama_bagian','sub_bagian']


    def __str__(self):
        return self.sub_bagian

# datatable notebook
class Notebook(models.Model):

    nama = models.CharField(('Nama'),max_length=100,null=True,blank=False,help_text='Nama Pengunjung')
    profesi = models.CharField(('Profesi'),max_length=100,null=True,blank=False,help_text='Profesi Pengunjung')
    no_telp = models.CharField(('Nomor Telp'),max_length=50,null=True,blank=False,help_text='Nomor Handphone untuk dihubungi')
    pertanyaan = models.TextField(('Pertanyaan'),null=True,blank=False,help_text='Pertanyaan Pengunjung' )
    kategori = models.CharField(('Kategori Pertanyaan'),max_length=100,help_text='Kategori Pertanyaan')
    bagian = models.ForeignKey(bagian,verbose_name =('Bagian'),on_delete=models.SET_NULL,null=True,default=None,help_text='Sub Bagian yang bertanggung jawab')
    prioritas = models.CharField(('Prioritas'),max_length=100,null=True,blank=False,help_text='Prioritas Masalah')
    jawaban = models.TextField(('Jawaban'),null=True,blank=False,help_text='Solusi atau jawaban')
    keterangan = models.BooleanField(('Keterangan'),default=False,help_text='Keterangan Masalah selesai atau belum selesai')

    created = models.DateTimeField(verbose_name=('Created'),auto_now_add=True)
    updated = models.DateTimeField(verbose_name=('Updated'),auto_now=True)


    class Meta:
        verbose_name = ('notebook')
        verbose_name_plural = ('notebooks')
        ordering = ['nama','kategori']


    def __str__(self):
        return self.title + ' | ' + str(self.keterangan)

# datatable catatan
class catatan(models.Model):

    catatan = models.TextField(('Catatan'),max_length=300,null=True,blank=False)
    kategori = models.CharField(('Kategori'),max_length=100,null=True,blank=False)

    created = models.DateTimeField(verbose_name=('Created'),auto_now_add=True)
    updated = models.DateTimeField(verbose_name=('Updated'),auto_now=True)

    def __str__(self):
        return self.catatan