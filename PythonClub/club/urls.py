from django.urls import path
from . import views

urlpatterns=[
        path('', views.index, name='index'),
	path('getmeetings/', views.getmeetings, name='meetings'),
	path('getresourses/', views.getresourses, name='resources'),
]

