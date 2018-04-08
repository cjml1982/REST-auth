# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone

class UserManager(BaseUserManager):
    
    def create_user(self, email, password):
        if not email:
            raise '邮箱地址不能为空'
        user = self.model(email=self.normalize_email(email), last_login=timezone.now())
        user.set_password(password)
        user.save(using=self._db)
        return user
        
        
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin=True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    
    email = models.EmailField(primary_key=True, max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    
    def is_staff(self):
        return self.is_admin
    
    def __unicode__(self):
        return self.email
    
    
    def has_module_perms(self, demo):
        return True

    
    def has_perm(self, perm, obj=None):
        return True
    
    
    def get_short_name(self):
        # The user is identified by their email address
        return self.email
    
    
    def get_full_name(self):
        # The user is identified by their email address
        return self.email




class Task(models.Model):
    title = models.CharField(max_length=100)
    person = models.ForeignKey(User, related_name='tasks')
    due_to = models.DateTimeField()
    
    def __unicode__(self):
        return self.title

