from django.db import models
from uuid import uuid4
from django.core.validators import MaxValueValidator, MinValueValidator

class Project(models.Model):
    '''Projects model'''
    
    project_type = [
        ('S', 'Single'),
        ('J', 'Joint'),
    ]
    
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    name = models.CharField(null=False, unique=True, max_length=200)
    description = models.TextField(null=False, max_length=250)
    overview = models.TextField(null=False, default='No overview for this project.')
    cover_picture = models.ImageField(null=True, upload_to='project', default='default.JPG')
    detail_cover_picture = models.ImageField(null=True, upload_to='project', default='default.JPG')
    tools = models.CharField(null=False, max_length=1000, default='')
    domain = models.CharField(null=False, max_length=100, default='')
    type_of_project = models.CharField(choices=project_type, null=False, max_length=20, default='S')
    role = models.CharField(null=False, max_length=200, default='')
    github_link = models.URLField(null=False)
    postman_docs_link = models.URLField(null=True)
    live_link = models.URLField(null=True)
    google_drive_link = models.URLField(null=True)
    figma_link = models.URLField(null=True)
    upload_date = models.DateField(null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-upload_date']
    

class Service(models.Model):
    '''Services model'''
    
    name = models.CharField(null=False, max_length=200)
    description = models.TextField(null=False)
    fontawesome_classname = models.CharField(null=False, max_length=150)
    relevant_skills = models.TextField(null=False)
    
    def __str__(self):
        return self.name
    

class Experience(models.Model):
    '''Work experience model'''
    
    company_name = models.CharField(null=False, max_length=200, unique=True)
    company_picture = models.ImageField(null=True, upload_to='experience', default='default.JPG')
    address = models.TextField(null=False)
    role = models.CharField(null=False, max_length=200)
    date_started = models.DateField(null=False)
    date_ended = models.DateField(null=True)
    
    def __str__(self):
        return self.company_name
    
    class Meta:
        ordering = ['-date_started']
        

class Education(models.Model):
    '''Education background model'''
    
    school_name = models.CharField(null=False, max_length=200, unique=True)
    school_picture = models.ImageField(null=True, upload_to='education', default='default.JPG')
    address = models.TextField(null=False)
    course_studied = models.CharField(null=False, max_length=200)
    grade = models.CharField(null=True, max_length=200)
    date_started = models.DateField(null=False)
    date_ended = models.DateField(null=True)
    
    def __str__(self):
        return self.school_name
    

class Award(models.Model):
    '''Awards model'''
    
    award = models.CharField(null=False, max_length=400)
    award_description = models.TextField(null=False)
    issuer = models.CharField(null=False, max_length=200)
    issuer_picture = models.ImageField(null=True, upload_to='award', default='default.JPG')
    date_received = models.DateField(null=False)
    
    def __str__(self):
        return self.award
    
    
class Certification(models.Model):
    '''Certifications model'''
    
    issuer = models.CharField(null=False, max_length=200)
    issuer_picture = models.ImageField(null=True, upload_to='certification', default='default.JPG')
    certification = models.CharField(null=False, max_length=200)
    issue_date = models.DateField(null=False)
    certification_number = models.CharField(null=True, max_length=200)
    certification_url = models.URLField(null=True)
    
    def __str__(self):
        return f'{self.issuer} || {self.certification}'
    

class Skill(models.Model):
    '''Skills model'''
    
    skill_name = models.CharField(null=False, max_length=200)
    proficiency = models.IntegerField(null=False, validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    
    def __str__(self):
        return f'{self.skill_name}- {self.proficiency}'
    
    class Meta:
        ordering = ['-proficiency']
        

class Contact(models.Model):
    '''Contact form model'''
    
    name = models.CharField(null=False, max_length=200)
    email = models.EmailField(null=False, max_length=200)    
    message = models.TextField(null=False)
    date_sent = models.DateTimeField(auto_now_add=True, null=False)
    
    def __str__(self):
        return f'{self.name} | {self.email} | {self.date_sent}'
    
    class Meta:
        ordering = ['-date_sent']
