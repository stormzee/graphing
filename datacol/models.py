from django.db import models


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Metrics_view(models.Model):
    sn = models.CharField(primary_key=True, max_length=50)
    country = models.CharField( max_length=255, blank=True, null=True)
    feature = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    # category = models.CharField(max_length=255, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    card = models.IntegerField(blank=True, null=True)
    has_card = models.IntegerField(blank=True, null=True)
    recall = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'metrics_view_home_checkvacc'