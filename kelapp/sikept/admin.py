from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Yayasan)
admin.site.register(Pts)
admin.site.register(Dokumen)
admin.site.register(Order)
admin.site.register(Tag)