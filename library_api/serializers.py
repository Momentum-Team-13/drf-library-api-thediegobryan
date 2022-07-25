from rest_framework import serializers
from .models import Book, Book_Record, Note, User

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'publish_year', 'featured',)

class BookRecordSerializer(serializers.ModelSerializer):
    # book =  BookSerializer()
    # user =  serializers.StringRelatedField()

    class Meta:
        model = Book_Record
        fields = ('id', 'status', 'user','book',)

class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ('user', 'book','page_number', 'note', 'public', 'created_at')