from django.db import models
from models.user import User

class Board(models.Model):
    board_id = models.AutoField(primary_key=True)
    board_title = models.TextField(max_length=255,blank=True)
    board_author = models.ForeignKey(User)
    board_delete = models.BooleanField(default=False)