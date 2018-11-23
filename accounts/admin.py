from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import MyUser
from .forms import UserAdminChangeForm,UserAdminCreationForm

class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email','first_name','last_name','admin','staff')#'first_name','last_name',
    list_filter = ('admin','staff','active')
    fieldsets = (
        (None,{'fields':('email','password')}),
        ('Personal info',{'fields':('first_name','last_name')}),#'first_name','last_name'
        ('Permissions',{'fields':('admin','staff','active')})
        )
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','first_name','last_name','password1','password2')}#'first_name','last_name',
         ),
        )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(MyUser,UserAdmin)
admin.site.unregister(Group)

