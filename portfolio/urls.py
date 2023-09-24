from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', view=views.HomeView.as_view(), name='home'),
    path('about/', view=views.AboutMeView.as_view(), name='about'),
    path('projects/', view=views.ProjectsView.as_view(), name='projects'),
    path('contact-me/', view=views.ContactMeView.as_view(), name='contact'),
    
    # id will be needed
    path('project/', view=views.GetProjectDetailsView.as_view(), name='project_details'),
]