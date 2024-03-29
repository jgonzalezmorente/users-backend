from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager



class User( AbstractBaseUser, PermissionsMixin ):

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )

    username  = models.CharField( max_length = 10, unique = True )
    email     = models.EmailField()
    firstname = models.CharField( max_length = 30, blank = True )
    lastname  = models.CharField( max_length = 30, blank = True )
    gender    = models.CharField( max_length = 1, choices = GENDER_CHOICES, blank = True )
    is_staff  = models.BooleanField( default = False )
    is_active = models.BooleanField( default = False )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [ 'email' ]

    objects = UserManager()


    def get_short_name( self ):
        return self.username

    def get_full_name( self ):
        return f'{ self.firstname } { self.lastname }'

    
