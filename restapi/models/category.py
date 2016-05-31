from django.db import models

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = True
        db_table = 'category'
        ordering = ('category_id',)