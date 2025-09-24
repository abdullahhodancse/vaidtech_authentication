from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError("Email Address must here")
        
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)


        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must be in true')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super user must be is_superuser=true')
        
        return self.create_user(email,password,**extra_fields)
    

class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=CustomUserManager()


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']



    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.email

    # PermissionsMixin এর groups ও user_permissions override করে related_name দিতে হবে
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # default clash avoid করার জন্য
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set_permissions',  # default clash avoid
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

        