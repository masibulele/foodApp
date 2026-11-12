
from django.urls import path
from . import views

app_name = 'foodApp'

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:id>/',views.details, name='details'),
    path('add/',views.create_item, name='add'),
    path('edit/<int:id>/',views.edit_item, name='edit'),
    path('delete/<int:id>/',views.delete_item, name='delete'),
]