from django.db import models

class Search(models.Model):
    search = models.CharField(max_length=100)

    class Meta:
        db_table = "search"

