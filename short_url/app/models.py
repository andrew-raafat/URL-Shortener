from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class ShortURL(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    original_url = models.URLField(max_length=2050, null=False, blank=False)
    short_url = models.CharField(max_length=7, unique=True, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    time_date_created = models.DateTimeField()

    def __str__(self):
        return str(self.user)
    

class Count(models.Model):
    counter = models.IntegerField()
    limit = models.IntegerField()

    def __str__(self):
        return str(self.counter)
    
