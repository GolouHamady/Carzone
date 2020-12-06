from django.contrib import admin
from django.utils.html import format_html
from . models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'city', 'email', 'phone', 'create_date')
    list_display_links = ('id', 'first_name')
    list_filter = ('city', 'first_name')
    search_fields = ('id', 'first_name', 'last_name', 'email', 'city')


admin.site.register(Contact, ContactAdmin)
