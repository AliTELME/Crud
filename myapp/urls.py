from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('form/', views.forms),
    path('student_list/', views.list),
    path('<int:id>/', views.Delete , name="delete"),
    path('<int:id>/Edit/', views.forms , name="edit"),
]
