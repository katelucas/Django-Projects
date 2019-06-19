from django.contrib import admin

# Register your models here.

from catalog.models import Author, Genre, Book, BookInstance

# admin.site.register(Book)
# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
admin.site.register(Genre)
# admin.site.register(Author)
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)
# admin.site.register(BookInstance)
# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')