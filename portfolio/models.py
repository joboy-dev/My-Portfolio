from django.db import models

class Project(models.Model):
    '''Project Model'''
    
    name = models.CharField(null=False, unique=True, max_length=100)
    description = models.TextField(null=False)
    cover_picture = models.ImageField(null=False, upload_to='cover_pictures', default='cover_pictures/default.JPG')
    github_link = models.URLField(null=False)
    postman_docs_link = models.URLField(null=True)
    live_link = models.URLField(null=True)
    
    def __str__(self):
        return f'{self.name}'
