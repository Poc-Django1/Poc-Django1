from django.db import models
from django.utils import timezone

class subjectdetails(models.Model):
    subject=models.CharField(max_length=30)
    Created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
