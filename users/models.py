from django.db import models

# Create your models here.
# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=300, blank=True)
    skills = models.ManyToManyField(Skill, blank=True, related_name='users')
    
    EXPERIENCE_LEVELS = [
        ('JR', 'Junior'),
        ('MD', 'Mid'),
        ('SR', 'Senior'),
        ('EX', 'Experto'),
    ]
    level = models.CharField(max_length=2, choices=EXPERIENCE_LEVELS, blank=True)

    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    discord = models.URLField(blank=True, null=True)
    
    
    friends = models.ManyToManyField('self', blank=True, symmetrical=True)

    def __str__(self):
        return self.username
