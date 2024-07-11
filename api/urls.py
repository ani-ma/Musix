 #imported main function from "musix\api\views.py"
from django.urls import path
from .views import RoomView

urlpatterns = [#If url is blank call the main function from views.py
    path("home",RoomView.as_view()), 
    #This class turns the url api/home into JSON data
]