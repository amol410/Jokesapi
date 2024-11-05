from django.db import models

# Create your models here.
from django.db import models

class Joke(models.Model):
    CATEGORY_CHOICES = [
        ('Any', 'Any'),
        ('Programming', 'Programming'),
        ('Misc', 'Miscellaneous'),
        ('Dark', 'Dark'),
        ('Pun', 'Pun'),
        ('Spooky', 'Spooky'),
        ('Christmas', 'Christmas'),
    ]
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    type = models.CharField(max_length=10)
    joke = models.TextField(null=True, blank=True)
    setup = models.TextField(null=True, blank=True)
    delivery = models.TextField(null=True, blank=True)
    nsfw = models.BooleanField(default=False)
    political = models.BooleanField(default=False)
    sexist = models.BooleanField(default=False)
    safe = models.BooleanField(default=True)
    lang = models.CharField(max_length=10)

    def __str__(self):
        return self.category
