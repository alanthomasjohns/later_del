from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser

from user.manager import UserManager




# Create your models here.
GENDER_CHOICES = (
    ('male', 'male'),
    ('female', 'female'),
    ('other', 'other')
)

class AccountManager(BaseUserManager) :
    def create_user(self, first_name, last_name, email, username, gender, dob, password=None) :
        if not first_name :
            raise ValueError("User must provide the first name")
        if not email :
            raise ValueError("User must provide an email")
        if not username :
            raise ValueError("User must provide a username")
        if not gender :
            raise ValueError("User must provide the gender")
        if not dob :
            raise ValueError("User must provide date of birth")
        
        
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            username = username,
            gender = gender,
            dob = dob
        )
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, first_name, last_name, email, username, gender, dob, password) :
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username= username,
            dob=dob,
            gender=gender,
            password=password
        )
        
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        
        user.save()
        return user
        
        

class Account(AbstractUser):

    gender_choices = (
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Custom', 'Custom')
    )
    username = None
    email = models.EmailField( unique=True)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6 , null=True, blank=True)
    birthday = models.DateField(null=True)
    gender = models.CharField(max_length=20, choices=gender_choices, null = True)
    profile_pic = models.ImageField(default='default_user.jfif', upload_to = 'profile_pics')
    cover_pic = models.ImageField(default='default_cover.jfif', upload_to = 'cover_pics')
    bio = models.TextField(blank=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    def name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.email
