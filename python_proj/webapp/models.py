from django.db import models

# Create your models here.
class WebappItem(models.Model):
    content = models.TextField()
