from django.db import models

class Project(models.Model):
    '''Project Model'''
    
    name = models.CharField(null=False, unique=True)
    description = models.TextField(null=False)
    github_link = models.URLField(null=False)
    postman_docs_link = models.URLField(null=True)
    live_link = models.URLField(null=True)
    
    def __str__(self):
        return f'{self.name}'
