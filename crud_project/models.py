from django.db import models
from django.utils import timezone
class Task(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateTimeField(default=timezone.now())
    STATUS_CHOICES = (
        ('com', 'Completed'),
        ('inp', 'In Progress'),
        ('fld', 'Failed'),
    )
    status = models.CharField(max_length=200,choices=STATUS_CHOICES)

    def __str__(self):
        return self.title


