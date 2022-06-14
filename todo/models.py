from django.db import models

# Create your models here.
class Todo(models.Model):
    label = models.CharField(max_length=255)
    due_date = models.DateTimeField(blank=True)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)
    
    def __str__(self):
        return self.label
    
    class Meta:
        ordering = ['due_date']
