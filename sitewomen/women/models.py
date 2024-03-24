from django.db import models



class Women(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)



    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-title']
        indexes = [
            models.Index(fields=['-title'])
        ]