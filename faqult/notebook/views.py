from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NotebookForm, CatatanForm, BagianForm
from .models import Notebook, catatan, bagian
from django.views.generic import ListView, DetailView
from django.contrib import messages
 
#home view for posts. Posts are displayed in a list
class IndexView(ListView):
    template_name='index.html'
    context_object_name='post_list'
    def get_queryset(self):
        return Notebook.objects.all()

class NotebookList(ListView):
    template_name='notebook_list.html'
    context_object_name='post_list'
    def get_queryset(self):
        return Notebook.objects.all()

#List View Untuk catatan
class CatatanList(ListView):
    template_name='catatan/catatan_list.html'
    context_object_name='cat_list'
    def get_queryset(self):
        return catatan.objects.all()

#List View Untuk catatan
class BagianList(ListView):
    template_name='bagian/bagian_list.html'
    context_object_name='bag_list'
    def get_queryset(self):
        return bagian.objects.all()

class NotebookDetailView(DetailView):
    model=Notebook
    template_name = 'notebook/notebook-detail.html'

@login_required
#New posting (Create new post)
def postview(request):
    if request.method == 'POST':
        form = NotebookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Informasi Berhasil ditambahkan.'))
            return redirect('notebook:Notebook_list')
    form = NotebookForm()
    return render(request,'notebook/post.html',{'form': form})

@login_required
#New posting (Create new post untuk catatan)
def catatanbaru(request):
    if request.method == 'POST':
        form = CatatanForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Informasi Berhasil ditambahkan.'))
            return redirect('notebook:Catatan_list')
    form = CatatanForm()
    return render(request,'catatan/catatan.html',{'form': form})

@login_required
#New posting (Create new post untuk catatan)
def catatanbaru(request):
    if request.method == 'POST':
        form = CatatanForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Informasi Berhasil ditambahkan.'))
            return redirect('notebook:Catatan_list')
    form = CatatanForm()
    return render(request,'catatan/catatan.html',{'form': form})

@login_required
#New bagian (Create new post untuk bagian)
def BagianBaru(request):
    if request.method == 'POST':
        form = BagianForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Informasi Berhasil ditambahkan.'))
            return redirect('notebook:Notebook_list')
    form = BagianForm()
    return render(request,'bagian/bagian.html',{'form': form})

@login_required
#Edit Bagian
def BagianEdit(request, id, template_name='bagian/edit.html'):
    post = get_object_or_404(Notebook, id=id)
    form = BagianForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, ('Informasi Berhasil diedit.'))
        return redirect('notebook:Bagian_list')
    return render(request, template_name, {'form':form})

@login_required
#Edit notebook
def EditNotebook(request, id, template_name='notebook/edit.html'):
    post = get_object_or_404(Notebook, id=id)
    form = NotebookForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, ('Informasi Berhasil diedit.'))
        return redirect('notebook:Notebook_list')
    return render(request, template_name, {'form':form})

@login_required
#Edit catatan
def EditCatatan(request, id, template_name='catatan/edit.html'):
    post = get_object_or_404(catatan, id=id)
    form = CatatanForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, ('Informasi Berhasil diedit.'))
        return redirect('notebook:Catatan_list')
    return render(request, template_name, {'form':form})

@login_required
#Edit catatan
def BagianEdit(request, id, template_name='bagian/edit_bagian.html'):
    post = get_object_or_404(bagian, id=id)
    form = BagianForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, ('Informasi Berhasil diedit.'))
        return redirect('notebook:Catatan_list')
    return render(request, template_name, {'form':form})

@login_required
def post_pending(request, id):
    post = get_object_or_404(Notebook, id=id)
    post.keterangan = True
    post.save()
    messages.success(request, ('Status Belum Selesai.'))
    return redirect('notebook:Notebook_list')

@login_required    
def post_completed(request, id):
    post = get_object_or_404(Notebook, id=id)
    post.keterangan = False
    post.save()
    messages.success(request, ('Status Selesai.'))
    return redirect('notebook:Notebook_list')