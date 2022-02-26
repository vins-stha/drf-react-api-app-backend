from django.db import models
from django.conf import settings

# Create your models here.


class Article(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    # user_id = models.ForeignKey('auth.User',
    #                             related_name='articles',
    #                             on_delete=models.CASCADE)
    # highlighted = models.TextField()
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['created']
