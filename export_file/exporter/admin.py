from django.contrib import admin
from .models import Book
from import_export.admin import ExportActionMixin

# Register your models here.
# @admin.register(Book)
class BookAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['title', 'description', 'author', 'year']

admin.site.register(Book, BookAdmin)
