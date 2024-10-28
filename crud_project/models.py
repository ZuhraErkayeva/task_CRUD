from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateTimeField(default=timezone.now())
    STATUS_CHOICES = (
        ('com', 'Completed'),
        ('inp', 'In Progress'),
        ('fld', 'Failed'),
    )
    status = models.CharField(max_length=200,choices=STATUS_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True)

    def __str__(self):
        return self.title


