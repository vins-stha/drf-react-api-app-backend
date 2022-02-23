from pyexpat import model
import stat
from django.db import models

TASK_STATUS = (
    ('Not-started', 'Not-Started'),
    ('Obgoing', 'Ongoing'),
    ('Completed', 'Completed')
)
# Create your models here.
class Tasks(models.Model):
    name = models.CharField(max_length=100, blank=False,help_text="Enter name for your task")
    
    description = models.TextField(max_length=500, blank=True)
    
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)

    status = models.CharField(
        max_length=20,
        blank=False,
        choices=TASK_STATUS,
        default='Not-started',
        help_text="Status of task"
        )
    
    created_at = models.DateTimeField(auto_now=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_at']
    def __str__(self):
        return self.name


class Users(models.Model):
    name = models.CharField(max_length=255, help_text="Enter username", blank=False)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=255, blank=False)
     
    class  Meta:
        db_table = 'users'
        constraints = [
            models.UniqueConstraint(fields=['email'], name='unique_email')
        ]
    
    def __str__(self):
        return f'{self.name} {self.email}'
    