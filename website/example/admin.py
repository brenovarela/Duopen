from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django import forms
from .models import Item


class ItemAdminForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_id', 'item_data']
        

class ItemAdmin(admin.ModelAdmin):
    form = ItemAdminForm
    list_display = ['item_id', 'item_data']
    change_list_template = "duopen_admin/item_changelist.html"


admin.site.register(Item, ItemAdmin)
