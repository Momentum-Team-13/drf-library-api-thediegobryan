from django.contrib import admin
from .models import Book, Book_Record, Note, User

# Register your models here.

admin.site.register(Book)
admin.site.register(Book_Record)
admin.site.register(Note)
admin.site.register(User)
