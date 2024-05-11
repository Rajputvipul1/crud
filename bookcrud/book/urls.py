from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    # Homepage - List of all books
    path('', views.book_list, name='book_list'),

    # Detail view for a specific book
    path('book/<int:pk>/', views.book_detail, name='book_detail'),

    # Create a new book
    path('book/new/', views.book_create, name='book_create'),

    # Update an existing book
    path('book/<int:pk>/edit/', views.book_update, name='book_update'),

    # Delete a book
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
