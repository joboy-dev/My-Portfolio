from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView
from django.core.mail import send_mail

from datetime import datetime
import smtplib
import os
from dotenv import load_dotenv
from pathlib import Path

from .forms import ContactForm, SearchProjectForm
from .models import Contact, Project


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

context = {
     'year': datetime.now().year
}

class HomeView(View):
    '''View for home page'''
    
    def get(self, request):
        context['active_link'] = 'home'
        return render(request, 'index.html', context)


class AboutMeView(View):
    '''View for about me page'''
    
    def get(self, request):
        context['active_link'] = 'about'
        return render(request, 'about-me.html', context)
    
    
class ProjectsView(View):
    '''View for projects page'''
    
    def get(self, request):
        form = SearchProjectForm()
        context['active_link'] = 'projects'
        context['form'] = form
        return render(request, 'projects.html', context)
    
    def post(self, request):
        # domain = request.POST['domain']
        form = SearchProjectForm(request.POST)
        
        if form.is_valid():
            domain = form.cleaned_data['domain']
            
            if domain == 'None':
                messages.error(request, 'Please select a domain')
            else:
                messages.success(request, f"Filtered by '{domain}'")
                
            return redirect(reverse_lazy('portfolio:projects'))
        
        return render(request, 'projects.html', context)
        
    

class ContactMeView(View):
    '''View for about me page'''
    
    def get(self, request):
        form = ContactForm()
        context['active_link'] = 'contact'
        context['form'] = form
        return render(request, 'contact-me.html', context)
    
    def post(self, request):
        form = ContactForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            date = datetime.now().strftime('%d %B, %Y | %H:%M')
            
            # add to database
            contact = Contact(
                name=name,
                email=email,
                message=message,
            )
            
            contact.save()
            
            try:
                smtp_email = os.getenv('SMTP_EMAIL')
                smtp_password = os.getenv('SMTP_PASSWORD')
                
                # connect to smtp and send email
                with smtplib.SMTP('smtp.gmail.com') as conn:
                    conn.starttls()
                    conn.login(user=smtp_email, password=smtp_password)
                    
                    # send mail
                    conn.sendmail(
                        from_addr=smtp_email, 
                        to_addrs='portfoliosite036@gmail.com',
                        msg=f"Subject:PORTFOLIO SITE!! - Message from {name}\n\nName:- {name}\nEmail:- {email}\nMessage- {message}\n\nMessage sent on {date}"
                    )
                        
                    messages.success(request, message='Message successfully sent.')
                    return redirect(reverse_lazy('portfolio:contact'))
            # catch exceptions
            except smtplib.SMTPException as smtp_exception:
                print(f'Exception: {smtp_exception}')
                
                messages.error(request, message='An error occured while trying to send your message. Please check your connection and try again.')
            except Exception as exception:
                print(f'Exception: {exception}')
                
                messages.error(request, message='An error occured while trying to send your message. Please try again.')
        else:
            messages.error(request, message='There was an error while trying to send your message. Please try again.')
        
        
        # form data will be rendered with the form
        context['form'] = form
        return render(request, 'contact-me.html', context)
    
    
# class GetProjectDetailsView(DetailView):
#     model = Project
#     template_name = ''

class GetProjectDetailsView(View):
    '''View to get project details'''
    
    def get(self, request):
        context['active_link'] = 'projects'
        
        return render(request, 'project-detail.html', context)
        

