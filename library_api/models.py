from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publish_year = models.PositiveIntegerField(null=True, blank=True)
    featured = models.BooleanField()

    def __str__(self):
        return f"{self.title} by {self.author}"


class Book_Record(models.Model):
    WANT = 'Want to read'
    READING = 'Reading'
    READ = 'Read'
    STATUS_CHOICES = [
        (WANT, 'Want to read'),
        (READING, 'Reading'),
        (READ, 'Read'),
    ]
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='user_book_records')
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name='book_book_records')
    status = models.TextField(choices=STATUS_CHOICES, default=WANT)

    def __str__(self):
        return f"{self.book}:{self.status}"

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_notes')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_notes') 
    note = models.TextField()
    public = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    page_number = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.book}:{self.note}"