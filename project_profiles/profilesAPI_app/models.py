from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

"""Manager for user profiles in the system"""
class UserProfileManager(BaseUserManager):
    """Create new user profile"""
    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email,name=name)

        user.set_password(password)
        user.save(using = self._db)

        return user

    """Create new Super user profile"""
    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


"""Database Model for users in the system"""
class UserProfile(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    """Retrieve Full name of user"""
    def get_full_name(self):
        return self.name
    
    """Retrieve short name of user"""
    def get_short_name(self):
        return self.name
    
    """Return string represenation of user"""
    def __str__(self):
        return self.email