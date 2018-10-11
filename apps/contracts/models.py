from django.contrib.postgres.fields import JSONField
from django.db import models


class Task(object):
    def __init__(self, **kwargs):
        for field in ('id', 'name', 'owner', 'status'):
            setattr(self, field, kwargs.get(field, None))


tasks = {
    1: Task(id=1, name='Demo', owner='xordoquy', status='Done'),
    2: Task(id=2, name='Model less demo', owner='xordoquy', status='Ongoing'),
    3: Task(id=3, name='Sleep more', owner='xordoquy', status='New'),
}


class Contract(models.Model):
    name = models.CharField(max_length=200)
    data = JSONField(default=dict)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Contract'
