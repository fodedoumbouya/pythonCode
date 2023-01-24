# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Contacts(models.Model):
    # Field name made lowercase.
    userid = models.CharField(db_column='userId', max_length=200)
    # Field name made lowercase.
    contactid = models.CharField(db_column='contactId', max_length=200)

    class Meta:
        managed = False
        db_table = 'contacts'


class Invitations(models.Model):
    # Field name made lowercase.
    userid = models.OneToOneField(
        'Users', models.DO_NOTHING, db_column='userId', primary_key=True)
    # Field name made lowercase.
    invitedid = models.CharField(db_column='invitedId', max_length=200)
    message = models.CharField(max_length=100, blank=True, null=True)
    blocked = models.IntegerField(blank=True, null=True)
    created = models.CharField(max_length=75)

    class Meta:
        managed = False
        db_table = 'invitations'


class Referencecode(models.Model):
    # Field name made lowercase.
    userid = models.CharField(
        db_column='userId', primary_key=True, max_length=200)
    code = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'referenceCode'


class Users(models.Model):
    # Field name made lowercase.
    userid = models.CharField(
        db_column='userId', primary_key=True, max_length=200)
    # Field name made lowercase.
    superuser = models.CharField(
        db_column='superUser', max_length=10, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    # Field name made lowercase.
    dialcode = models.CharField(db_column='dialCode', max_length=45)
    number = models.CharField(unique=True, max_length=65)
    url = models.TextField(blank=True, null=True)
    tag = models.CharField(max_length=45, blank=True, null=True)
    # Field name made lowercase.
    deviceid = models.CharField(db_column='deviceId', max_length=85)
    created = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
        unique_together = (('userid', 'number'),)
