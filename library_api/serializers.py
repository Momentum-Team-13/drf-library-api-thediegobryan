from rest_framework import serializers
from .models import Book, Book_Record, Note, User

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'publish_year', 'featured',)
