from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import UserManager as DjangoUserManager
from django.db import models


class UserManager(DjangoUserManager):
    def own(self, queryset=None):
        queryset = super(UserManager, self).own(queryset)
        return queryset


class UserDefaultManager(models.Manager):
    def get_by_natural_key(self, user_name):
        return self.get(**{self.model.USERNAME_FIELD: user_name})


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255, blank=False, unique=True)
    email = models.CharField(max_length=255, blank=False)
    is_staff = models.BooleanField(default=1)
    is_active = models.BooleanField(default=1)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.user_name

    objects = UserManager()
    objects_raw = UserDefaultManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email']

    class Meta:
        app_label = 'restapi'
        db_table = 'user'
        ordering = ('user_id',)
        unique_together = ('email', 'user_name')

    def is_authenticated(self):
        return self.user_name

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        if self.password == raw_password:
            return True
        else:
            return False
            # def setter(raw_password):
            #     self.set_password(raw_password)
            #     self.save(update_fields=['password'])
            # return check_password(raw_password, self.password, setter)


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
