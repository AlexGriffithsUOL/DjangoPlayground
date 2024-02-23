from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

class Item2(models.Model):
    name = models.CharField(max_length=20, blank=True)
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    description = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    orders = models.IntegerField(blank=True)
    image = models.ImageField(blank=True)

    def get_absolute_url(self):
        return reverse('shopping:detail', args=self.slug)
    
    def save(self, *args, **kwargs):
        # if not self.slug:
        self.slug = slugify(self.name)
        super(Item2, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return self.name
        
        def __str__(self):
            return self.name