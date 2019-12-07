from django import forms
from . models import Notebook, catatan, bagian

class NotebookForm(forms.ModelForm):

    class Meta:
        model = Notebook
        fields = "__all__"

class CatatanForm(forms.ModelForm):

    class Meta:
        model = catatan
        fields = "__all__"

class BagianForm(forms.ModelForm):

    class Meta:
        model = bagian
        fields = "__all__"
