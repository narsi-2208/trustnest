from django.db import models

class Mentor(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    background = models.CharField(max_length=150)
    current_role = models.CharField(max_length=150)
    linkedin = models.URLField(blank=True)
    bio = models.TextField()
    offers_mentoring = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

class CareerSwitcher(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    current_background = models.CharField(max_length=150)
    target_role = models.CharField(max_length=150)
    motivation = models.TextField()

    def __str__(self):
        return self.full_name



class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


    



