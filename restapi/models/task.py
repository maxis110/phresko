from django.db import models

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = True
        db_table = 'task'
        ordering = ('task_id',)