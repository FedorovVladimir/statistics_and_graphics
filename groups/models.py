from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)
    count_users = models.IntegerField()
    academic_performance = models.IntegerField()