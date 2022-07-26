"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path 
from library_api import views as lib_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lib_views.BookList.as_view(), name="homepage"), 
    path('books/', lib_views.BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', lib_views.BookDetail.as_view(), name='book-detail'),
    path('book_record/', lib_views.Book_Record_List.as_view(), name="book-record-list"),
    path('book_record/<int:pk>', lib_views.Book_Record_Detail.as_view(), name="book-record-detail"),
    path('notes/', lib_views.NoteList.as_view(), name='note-list'),
    path('notes/<int:pk>/', lib_views.BookDetail.as_view(), name='note-detail'),
]