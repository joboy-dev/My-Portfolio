from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Project)
admin.site.register(models.Service)
admin.site.register(models.Experience)
admin.site.register(models.Education)
admin.site.register(models.Award)
admin.site.register(models.Certification)
admin.site.register(models.Contact)


from django.core.management.utils import get_random_secret_key 
SECRET_KEY = get_random_secret_key()