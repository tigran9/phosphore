from django.contrib.postgres.fields import JSONField
from django.db import models


class Contract(models.Model):
    name = models.CharField(max_length=200)
    data = JSONField(default=dict)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Contract'
