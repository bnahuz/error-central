from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.hashers import make_password
import datetime

class User(models.Model):

    class Meta:

        db_table = 'user'
        ordering = ['id']

    name = models.CharField(("name"), max_length=50)
    last_login = models.DateField(default=datetime.date.today)
    email = models.EmailField(("email"), max_length=254, unique= True)
    password = models.CharField(max_length=50, validators=[MinLengthValidator(8)])
    acess_token = models.CharField(max_length=254)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)


    def __str__(self):
        return self.name
