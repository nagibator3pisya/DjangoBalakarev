from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    """
    будет возвращать только публикованные записи
    """

    def get_queryset(self):
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)



class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0,'Черновик'
        PUBLISHED = 1, 'Опубликован'

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255,unique=True,db_index=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)



    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-title']
        indexes = [
            models.Index(fields=['-title'])
        ]


    def get_absolute_url(self):
        """формирование юрл для каждой записи"""
        return reverse('post', kwargs={'post_slug': self.slug})