from django.urls import path

from . import views

urlpatterns = [
    path('', views.trainee_list, name='trainee_list'),
    path('add/', views.trainee_add, name='trainee_add'),
    path('<int:id>/', views.trainee_detail, name='trainee_detail'),
    path('update/<int:id>/', views.trainee_update, name='trainee_update'),
    path('delete/<int:id>/', views.trainee_delete, name='trainee_delete'),
]
