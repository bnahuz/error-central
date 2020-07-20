from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.hashers import make_password
import datetime

class User(models.Model):

    class Meta:

        db_table = 'user'
        ordering = ['id']

    name = models.CharField(("name"), max_length=50)
    last_login = models.DateField(("last_login"), auto_now_add=True)
    email = models.EmailField(("email"), max_length=254, unique= True)
    password = models.CharField(max_length=50, validators=[MinLengthValidator(8)])
    acess_token = models.CharField(max_length=254)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)


    def __str__(self):
        return self.name

class Events(models.Model):

    class Meta:

        db_table = 'events'
        ordering = ['error_date']

    EVENT_CHOICES = (
        ("D", "Dev"),
        ("P", "Produção"),
        ("H", "Homologação")
    )

    LEVEL_CHOIVES = (
        ('ERROR'),
        ('DEBUG'),
        ('WARING')
    )

    title = models.CharField(("Event Title"), max_length=50, blank=False, null=False)
    detail = models.TextField(("Detail"), blank=False, null=False)
    quantity = models.IntegerField(("Quantity"),blank=False, null=False)
    level = models.CharField(("Level"), max_length=1, choices = EVENT_CHOICES, blank=False, null=False)
    event_type = models.CharField(("Type"), max_length=1, choices = EVENT_CHOICES, blank=False, null=False)
    error_date = models.DateField(("Error Date"), auto_now_add=True)
    colected_by = models.ForeignKey(User.acess_token, verbose_name=_(""), on_delete=models.CASCADE)
    archived = models.BooleanField()

    def __str__(self):
        return self.title