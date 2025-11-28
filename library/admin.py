from django.contrib import admin
from .models import Book
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title","author","started_on","finished_on","rating")
    search_fields = ("title","author")