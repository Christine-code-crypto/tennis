from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name='main'),
    path('members/',views.members, name='members' ),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/',views.testing, name='testing'),
    path('testing1/',views.testing1, name='testing1'),
    path('testing2/',views.testing2, name='testing2'),
    path('testing3/',views.testing3, name='testing3'),
]