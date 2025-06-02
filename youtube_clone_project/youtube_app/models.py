from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Upload(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(null=True, blank=True)
    video = models.FileField(upload_to='videos')
    thumbnail = models.ImageField(upload_to='thumbnail', null=True, blank=True)
    views = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
