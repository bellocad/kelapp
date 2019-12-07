from django.contrib import admin
from notebook.models import Notebook,bagian #add this to import the Post model


class NotebookAdmin(admin.ModelAdmin):
    list_display = ('nama','kategori')

class bagianAdmin(admin.ModelAdmin):
    list_display = ('nama_bagian','sub_bagian')

admin.site.register(Notebook, NotebookAdmin) #add this to register the Post model
admin.site.register(bagian, bagianAdmin)