from .views import main #imported main function from "musix\api\views.py"
from django.urls import path

urlpatterns = [
    path("",main) #If url is blank call the main function from views.py
]