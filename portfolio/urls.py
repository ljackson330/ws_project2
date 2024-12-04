from django.urls import path

from . import views

app_name = 'portfolio'

urlpatterns = [
    path("", views.index, name="index"),
    path('edit/<int:project_id>/', views.edit_project, name='edit_project'),
    path('delete/<int:project_id>/', views.delete_project, name='delete_project'),
    path('create/', views.create_project, name='create_project'),
]