from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Project(models.Model):
    class Categories(models.TextChoices):
        WEB_APP = 'W', 'Web applications'
        OTHERS = 'O', 'Others application'

    category = models.CharField(max_length=1, choices=Categories.choices, default=Categories.WEB_APP)
    name = models.CharField(max_length=128)
    slug = models.SlugField(blank=True)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=256, blank=True)
    keywords_list = models.CharField(max_length=256, blank=True)
    url_github_oc = models.URLField(max_length=200, blank=True, null=True)
    url_github_portfolio = models.URLField(max_length=200, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='projects', blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'slug': self.slug})
