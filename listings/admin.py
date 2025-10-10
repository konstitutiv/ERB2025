from django.contrib import admin

# Register your models here.

from .models import Listing, Subject
from django.forms import NumberInput
from django.db import models

from django import forms
from taggit.forms import TagWidget
from django.contrib.admin.widgets import FilteredSelectMultiple

class ListingsAdminForm(forms.ModelForm):

    subjects = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=FilteredSelectMultiple(verbose_name='Professionals', is_stacked=False,attrs={'rows': 5}),required=False, label='Select Professionals'
    )


    class Meta:
        model = Listing
        fields = [
            'doctor','title','address','district','description','services','service','room_type','screen','professionals','professional','rooms','photo_main','photo_1','photo_2','photo_3','photo_4','photo_5','photo_6','is_published',
        ]
        widgets = {
            'services': TagWidget(),
        }

class ListingAdmin(admin.ModelAdmin):
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
    return super().get_queryset(request).prefetch_related('services','professionals')

def display_professionals(self, obj):
    return ", ".join([subject.name for subject in obj.subjects.all()])
display_professionals.short_description = "Prodessionals"

class SubjectAdmin(admin.ModelAdmin):
    list_display = "name",
    search_dields = ('name',)


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Listing, ListingAdmin)