from django.urls import path

from . import views

urlpatterns = [
    path("trainees/", views.trainee_list, name="api_trainee_list"),
    path("trainees/<int:id>/", views.trainee_detail, name="api_trainee_detail"),
    path("trainees/create/", views.TraineeCreateAPIView.as_view(), name="api_trainee_create"),
    path("trainees/update/<int:id>/", views.TraineeUpdateAPIView.as_view(), name="api_trainee_update"),
    path("trainees/delete/<int:id>/", views.TraineeDestroyAPIView.as_view(), name="api_trainee_delete"),
]
