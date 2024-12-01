from django.db import models
from django.contrib.auth.models import  AbstractUser, BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None,**extra_fields):
        if not email:
            raise  ValueError("Email must be a valid email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff =True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")
        return self.create_user(email,password,**extra_fields)

class Users(AbstractUser):
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=90, null=True, blank=True)
    last_name = models.CharField(max_length=90, null=True, blank=True)
    google_api_key = models.CharField(max_length=90, null=True, blank=True)
    profile_pic = models.FileField(upload_to="profile_pic", null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email
