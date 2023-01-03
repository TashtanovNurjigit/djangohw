from django.urls import path
from . import views

app_name = 'parse'

urlpatterns = [
    path('parser_book/', views.MyBookFormView.as_view(), name='parse_func'),
    path('parser_book_info/', views.MyBookView.as_view(), name='parse_view'),
]
