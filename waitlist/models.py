from django.db import models
from django.core.validators import EmailValidator

class WaitlistEntry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    preferences = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class CommunityPost(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100, blank=True, default="Anonymous")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.created_at}"