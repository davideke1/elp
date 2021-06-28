from django.db import models
from .user_manager import UserManager
from django.contrib.auth.base_user import AbstractBaseUser


# Create your models here.

############################# account section ############################
class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField( default=True)
    firts_name = models.CharField(max_length=400,blank=True)
    other_names = models.CharField(max_length=400,blank=True)
    contact = models.CharField(max_length=400,blank=True)
    gender = models.CharField(max_length=400,blank=True)
    location = models.CharField(max_length=400,blank=True)

    staff       = models.BooleanField(default=False) ##########3 For django staff user
    admin       = models.BooleanField(default=False)##########3 For jango adminuser
      
    vendor_status = models.BooleanField(default=False)
    Customer_status = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):

        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active



################################ vendor's account #################################