from django.contrib import admin

# Register your models here.

from .models import Listing
from django.forms import NumberInput
from django.db import models

from django import forms
from taggit.forms import TagWidget

class ListingsAdminForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = [
            'doctor','title','address','district','description','services','service','screens','screen','professionals','professional','rooms','photo_main','photo_1','photo_2','photo_3','photo_4','photo_5','photo_6','is_published',
        ]
        widgets = {
            'services': TagWidget(),
        }

class ListingsAdmin(admin.ModelAdmin):
    form = ListingsAdminForm
    list_display = 'id','title','district','is_published','doctor','tag_list'
    list_display_links = 'id','title'
    list_filter = 'doctor',
    list_editable = ('is_published',)
    search_fields = 'title','district','doctor__name','services__name'
    list_per_page = 25
    ordering = ['-id']
    prepopulated_fields = {"title" : ('title',)}
    formfield_overrides = {
        models.IntegerField:{
            'widget': NumberInput(attrs={'size':10})
        }
    }

show_facets = admin.ShowFacets.ALWAYS

def get_queryset(self,request):
    return super().get_queryset(request).prefetch_related('services')

admin.site.register(Listing,ListingsAdmin)