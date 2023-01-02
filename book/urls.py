from django.urls import path
from . import views

urlpatterns = [
    # path('book/', views.book_view, name='book'),
    path('book/', views.BookView.as_view(), name='book'),
    path('book_details/<int:id>/', views.BookDetailsView.as_view(), name='details'),
    path('book_details_/<int:id>/update/', views.BookUpdateView.as_view(), name='update'),
    path('book_details_/<int:id>/delete/', views.BookDeleteView.as_view(), name='delete'),
    path('add_book/', views.BookCreateView.as_view(), name='create_tv_show'),

]