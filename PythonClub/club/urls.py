from django.urls import path
from . import views

urlpatterns=[
        path('', views.index, name='index'),
	path('getmeetings/', views.getmeetings, name='meetings'),
	path('meetingdetails/<int:id>', views.meetingdetails, name='meetingdetails'),
	path('getminutes/', views.getminutes, name='minutes'),
	path('getresources/', views.getresources, name='resources'),
	path('getevents/', views.getevents, name='events'),
	path('newMeeting/', views.newMeeting, name='newmeeting'),
	path('newEvent/', views.newEvent, name='newevent'),
]

