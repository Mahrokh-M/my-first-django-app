from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("details/<int:person_id>/", views.details, name="details"),
    path("deletes/<int:person_id>/", views.delete, name="delete"),
    path("update/<int:person_id>/", views.update_user, name="update"),
    path("create/", views.create_user, name="create"),
]
