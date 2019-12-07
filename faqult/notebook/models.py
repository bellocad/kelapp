from django.db import models

# database bagian
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

# database notebook
class Notebook(models.Model):

    nama = models.CharField(('Nama'),max_length=100,null=True,blank=False)
    profesi = models.CharField(('Profesi'),max_length=100,null=True,blank=False)
    no_telp = models.CharField(('Nomor Telp'),max_length=50,null=True,blank=False)
    pertanyaan = models.TextField(('Pertanyaan'),null=True,blank=False)
    kategori = models.CharField(('Kategori Pertanyaan'),max_length=100)
    bagian = models.ForeignKey(bagian,verbose_name =('Sub Bagian'),on_delete=models.SET_NULL,null=True,default=None)
    prioritas = models.CharField(('Prioritas'),max_length=100,null=True,blank=False)
    jawaban = models.TextField(('Jawaban'),null=True,blank=False)

    created = models.DateTimeField(verbose_name=('Created'),auto_now_add=True)
    updated = models.DateTimeField(verbose_name=('Updated'),auto_now=True)


    class Meta:
        verbose_name = ('notebook')
        verbose_name_plural = ('notebooks')
        ordering = ['nama','kategori']


    def __str__(self):
        return self.nama

