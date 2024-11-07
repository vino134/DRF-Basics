from django.urls import path
from .views import *

urlpatterns=[
    path('product/',ProductView.as_view()),
    path('product/<int:id>/',ProductViewById.as_view()),

    path('catagory/',CatagoryView.as_view()),
    path('catagory/<int:id>/',CatagoryViewById.as_view())
]