from django import forms

class ItemForm(forms.Form):
    item_id = forms.CharField(label='Item ID', max_length=100)
