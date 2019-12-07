from django import forms
from . models import Notebook, catatan

class NotebookForm(forms.ModelForm):

    class Meta:
        model = Notebook
        fields = "__all__"

class CatatanForm(forms.ModelForm):

    class Meta:
        model = catatan
        fields = "__all__"