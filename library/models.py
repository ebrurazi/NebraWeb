from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=120, blank=True)
    started_on = models.DateField(null=True, blank=True)
    finished_on = models.DateField(null=True, blank=True)
    rating = models.PositiveSmallIntegerField(null=True,blank=True)
    notes = models.TextField(blank=True)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bookd",
        null=True,
        blank=True,
    )
    def __str__(self):
        return f"{self.title} - {self.author}".strip(" -")