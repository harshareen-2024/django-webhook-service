from django.db import models
from django.contrib.auth.models import User


class Webhook(models.Model):
    url = models.URLField()
    event_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_type


class Account(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Destination(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class AccountMember(models.Model):  # ✅ Add this class if missing
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=50, choices=[("admin", "Admin"), ("user", "User")]
    )
