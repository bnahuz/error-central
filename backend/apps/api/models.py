from django.db import models

from apps.login.models import User

class Event(models.Model):

    class Meta:

        db_table = 'events'
        ordering = ['error_date']

    EVENT_CHOICES = (
        ("D", "Dev"),
        ("P", "Produção"),
        ("H", "Homologação")
    )

    LEVEL_CHOICES = (
        ('ERROR','ERROR'),
        ('DEBUG','DEBUG'),
        ('WARING','WARING')
    )

    title = models.CharField(("Event Title"), max_length=50, blank=False, null=False)
    detail = models.TextField(("Detail"), blank=False, null=False)
    quantity = models.IntegerField(("Quantity"),blank=False, null=False)
    level = models.CharField(("Level"), max_length=6, choices = LEVEL_CHOICES, blank=False, null=False)
    event_type = models.CharField(("Type"), max_length=1, choices = EVENT_CHOICES, blank=False, null=False)
    error_date = models.DateField(("Error Date"), auto_now_add=True)
    colected_by = models.ForeignKey(User, verbose_name=(""), on_delete=models.CASCADE)
    archived = models.BooleanField()

    def __str__(self):
        return self.title