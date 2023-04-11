from django.urls import path

from contacts import views

urlpatterns = [
    path("contact", views.contact, name="contact")
]
