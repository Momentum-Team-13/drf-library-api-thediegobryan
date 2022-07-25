
from rest_framework import generics
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Book, Book_Record, Note, User
from .serializers import BookSerializer, BookRecordSerializer, NoteSerializer

class BookList(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class Book_Record_List(ListCreateAPIView):
    queryset = Book_Record.objects.all()
    serializer_class = BookRecordSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class Book_Record_Detail(RetrieveUpdateDestroyAPIView):
    queryset = Book_Record.objects.all()
    serializer_class = BookRecordSerializer

class NoteList(ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NoteDetail(RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer