from django.db import models
from models.user import User
from models.board import Board

class Record(models.Model):
    record_id = models.AutoField(primary_key=True)
    comment = models.TextField(max_length=255,blank=True)
    record_title = models.TextField(max_length=255,required=True)
    create_at = models.DateTimeField(auto_now_add=True)
    record_author = models.ForeignKey(User)
    parent_board = models.ForeignKey(Board)
    record_delete = models.BooleanField(default=False)