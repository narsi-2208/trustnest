from django.db import models
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    password_hash = models.TextField()
    location = models.TextField(help_text="City / Area / Pincode")
    # created_at = models.DateTimeField(auto_now_add=True)  # Removed as requested

    def __str__(self):
        return self.full_name


class Helper(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    gender = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    location = models.TextField(help_text="Available area / Pincode")
    skills = models.JSONField(help_text="Example: ['nurse', 'childcare', 'cook']")
    experience_years = models.PositiveIntegerField()
    languages = models.JSONField(help_text="Example: ['Hindi', 'Telugu']")
    documents = models.JSONField(help_text="e.g. {'aadhar': 'url', 'certificate': 'url'}")
    rating = models.FloatField(default=0.0)
    availability = models.JSONField(help_text="e.g. {'mon': ['9am-1pm'], 'tue': ['full_day']}")

    def __str__(self):
        return self.full_name
