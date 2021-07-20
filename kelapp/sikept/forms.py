from django.forms import ModelForm, forms
from . models import Order, Dokumen

class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['nomor'].queryset = self.fields['nomor'].queryset.order_by('-date_created')

class DokumenForm(ModelForm):
    class Meta:
        model = Dokumen
        fields = '__all__'

    def clean_nomor(self): #validate the nomor fields
        nomor = self.cleaned_data.get('nomor')
        if (nomor == ""):
            raise forms.ValidationError('Tidak Boleh Kosong')

        for instance in Dokumen.objects.all():
            if instance.nomor == nomor:
                raise forms.ValidationError(' _______________ Dokumen dengan nomor ' +       nomor +' sudah ada')
        return nomor



    