from django.urls import path

from .views import create_view, list_view, update_view, delete_view, export_to_pdf

app_name = 'poll'

urlpatterns = [
    path('', list_view, name='list'),
    path('create/', create_view, name='create'),
    path('update/<id>/', update_view, name='update'),
    path('delete/<id>/', delete_view, name='delete'),
    path('pdf/<id>/', export_to_pdf, name='pdf'),
]
