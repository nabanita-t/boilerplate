from django.contrib import admin
from .models import Book, Table, TableReservation, Customer, UrlArchive

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn')

@admin.register(Table)
class BookAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'capacity', 'location')


@admin.register(TableReservation)
class BookAdmin(admin.ModelAdmin):
    list_display = ('table', 'date', 'start_time', 'end_time')

@admin.register(Customer)
class BookAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number')

@admin.register(UrlArchive)
class UrlArchiveAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'shortened_url')
