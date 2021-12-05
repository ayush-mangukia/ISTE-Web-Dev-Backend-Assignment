from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']
