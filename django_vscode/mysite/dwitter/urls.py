from django.urls import path
from .views import dashboard, profile_list, profile

app_name = "dwitter"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("pofile/<int:pk>", profile, name='profile')     # int:pk is to specify that any integeger after profile/ should be funneled to the profile view function
]
