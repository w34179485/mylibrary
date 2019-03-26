from django.contrib import admin
from .models import Library,Book,Author,Reader,Record

class LibraryAdmin(admin.ModelAdmin):
    list_display = ['library_name','library_address','library_phone']

class BookAdmin(admin.ModelAdmin):
    list_display = ['book_name','book_price','book_amount','author']

class BookInline(admin.TabularInline):
    model = Book
    extra = 5

class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]

class ReaderAdmin(admin.ModelAdmin):
    list_display = ['reader_name','reader_sex','reader_phone','reader_money']

admin.site.register(Library,LibraryAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Reader,ReaderAdmin)
