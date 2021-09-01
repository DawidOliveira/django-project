from django.urls import path
from api import views

urlpatterns = [
  path("", views.ListUserAPIView.as_view(), name="user_list"),
  path("create/", views.CreateUserAPIView.as_view(), name="user_create"),
  path("update/<int:pk>/", views.UpdateUserAPIView.as_view(), name="user_update"),
  path("delete/<int:pk>/", views.DeleteUserAPIView.as_view(), name="user_delete")
]