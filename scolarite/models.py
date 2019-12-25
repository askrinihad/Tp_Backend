from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """Helps django work with our custom user model."""

    def create_user(self , email , name , password=None):
       """Creates a new user profile object."""
       if not email :
          raise ValueError ('Les utilisateurs doivent avoir un email .')

       email = self.normalize_email(email)
       user =  self.model(email=email , name=name)

       user.set_password(password)
       user.save(using=self._db)

       return user





    def create_superuser(self , email , name , password):
        """Creates and saves a new superuser with given details"""
        user = self.create_user(email , name , password)
        user.is_superuser =True
        user.is_staff = True

        user.save(using=self._db)
        return user




class UserProfile(AbstractBaseUser , PermissionsMixin):
    """Represents user profile inside our system"""
    email = models.EmailField(max_length=255 , unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    def __str__(self) :
      """django uses this when it needs to convert the object to a string"""
      return self.email


   #def get_full_name(self):
    #   """Used to get a users full name."""
     #  return self.name

class Etudiant(models.Model):
    matricule=models.CharField(max_length=8)
    nom=models.CharField(max_length=15)
    prenom = models.CharField(max_length=15)
    sect=models.CharField(max_length=5)
    groupe=models.IntegerField()
    photo_et=models.CharField(max_length=1000)
    niv=models.CharField(max_length=4)
def _str_(self):
    return self.photo_et + self.nom + '-' + self.prenom

class Module(models.Model):
    code_mod=models.CharField(max_length=8)
    niv=models.CharField(max_length=3)
    sem=models.IntegerField()
    nom=models.CharField(max_length=15)



class Enseignant(models.Model):
        code_ens = models.CharField(max_length=8)
        nom_ens = models.CharField(max_length=16)
        prenom_ens = models.CharField(max_length=15)
        niv = models.CharField(max_length=3)
        groupe = models.IntegerField()
        code_module=models.CharField(max_length=8)
        photo_ens = models.CharField(max_length=1000)

class Note(models.Model):
    matricule=models.CharField(max_length=8)
    code_mod = models.CharField(max_length=8)
    ci=models.FloatField()
    cc = models.FloatField()
    cf = models.FloatField()

class Charge_scolarite(models.Model):
    code_ch = models.CharField(max_length=8)
    nom_ch=models.CharField(max_length=15)
    prenom_ch = models.CharField(max_length=15)
    photo_ch = models.CharField(max_length=1000)


class ProfileFeedItem(models.Model):
     """Profile status update"""


     user_profile = models.ForeignKey('UserProfile' , on_delete = models.CASCADE)
     status_text = models.CharField(max_length=255)
     created_on = models.DateTimeField(auto_now_add= True)

     def __str__(self):
         """return the model as a string"""
         return self.status_text

