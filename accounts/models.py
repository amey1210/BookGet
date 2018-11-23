from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class MyUserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self,email,first_name,last_name,password=None):
        if not email:
            raise ValueError('Users must have an email address')
            first_name = first_name,
            last_name = last_name,
        user = self.model(
            email = self.normalize_email(email)
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self,email,first_name,last_name,password):
        user = self.create_user(email,first_name,last_name,password = password)
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self,email,first_name,last_name,password):
        user = self.create_user(email,first_name,last_name,password = password)#,first_name,last_name
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name = 'Email address',
        max_length = 255,
        unique = True
        )
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    active = models.BooleanField(default = True)
    staff = models.BooleanField(default = False)
    admin = models.BooleanField(default = False)
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']#'first_name','last_name'

    def get_full_name(self):
        return self.first_name+' '+self.last_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
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


