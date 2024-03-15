from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('', views.index, name='index'),
    path('past_events/',views.past_events,name="past_events")
]
