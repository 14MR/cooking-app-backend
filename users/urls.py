from django.urls import path

from users import views

urlpatterns = [path("profile/", views.ProfileAPIView.as_view(), name="profile")]
