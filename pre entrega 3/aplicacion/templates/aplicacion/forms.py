from django import forms

class ContactoForm(forms.form):
    nombre= forms.CharField(label="Nombre", max_length=50, required=True)
    comision = forms.IntegerField(label="comision", required=True)