from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = True
        db_table = 'user'
        ordering = ('user_id',)
        unique_together = ('email', 'user_name')


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = True
        db_table = 'category'
        ordering = ('category_id',)


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = True
        db_table = 'task'
        ordering = ('task_id',)
