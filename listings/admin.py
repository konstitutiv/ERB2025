from django.contrib import admin

# Register your models here.

from .models import Listing
from django.forms import NumberInput
from django.db import models

class ListingsAdmin(admin.ModelAdmin):
    list_display = 'id','title','district','is_published','doctor'
    list_display_links = 'id','title'
    list_filter = 'doctor',
    list_editable = ('is_published',)
    search_fields = 'title','district','doctor'
    list_per_page = 25
    ordering = ['-id']
    prepopulated_fields = {"title" : ('title',)}
    formfield_overrides = {
        models.IntegerField:{
            'widget': NumberInput(attrs={'size':10})
        }
    }

admin.site.register(Listing,ListingsAdmin)