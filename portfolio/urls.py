from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', view=views.HomeView.as_view(), name='home'),
    path('about/', view=views.AboutMeView.as_view(), name='about')
]