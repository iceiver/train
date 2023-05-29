# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Order(models.Model):
    train_id = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    from_field = models.CharField(db_column='from', max_length=50)  # Field renamed because it was a Python reserved word.
    to = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    user_card = models.CharField(max_length=50, blank=True, null=True)
    box_name = models.CharField(max_length=50,blank=True, null=True)
    seat_id = models.IntegerField(blank=True, null=True)
    seat_name = models.CharField(max_length=50, blank=True, null=True)
    user_phone = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order'


class Passby(models.Model):
    train_id = models.CharField(max_length=50, blank=True, null=True)
    station_id = models.CharField(max_length=30)
    arrival_time = models.DateTimeField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    time_consuming = models.CharField(max_length=50, blank=True, null=True)
    root = models.IntegerField(blank=True, null=True)
    next_id = models.IntegerField(blank=True, null=True)
    arrive = models.IntegerField(blank=True, null=True)
    current = models.IntegerField(blank=True, null=True)
    arrival_tim = models.DateTimeField(blank=True, null=True)
    start_tim = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'passby'


class Passenger(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'passenger'


class Refund(models.Model):
    tiid = models.CharField(primary_key=True, max_length=8)
    slid = models.CharField(max_length=50, blank=True, null=True)
    returnprice = models.DecimalField(max_digits=9, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refund'


class Seat(models.Model):
    train_id = models.CharField(max_length=50, blank=True, null=True)
    carriage_number = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    box = models.CharField(max_length=50, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seat'


class Staff(models.Model):
    slid = models.CharField(primary_key=True, max_length=50)
    slna = models.CharField(max_length=50)
    slpa = models.CharField(max_length=50)
    sname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'staff'


class Station(models.Model):
    sname = models.CharField(primary_key=True, max_length=50)
    scna = models.CharField(max_length=50, blank=True, null=True)
    spr = models.CharField(max_length=12, blank=True, null=True)
    slid = models.CharField(max_length=50, blank=True, null=True)
    id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'station'
        unique_together = (('sname', 'id'),)


class TickMange(models.Model):
    tiid = models.CharField(primary_key=True, max_length=8)
    tiss = models.CharField(max_length=50)
    tias = models.CharField(max_length=50)
    tist = models.DateField()
    tiat = models.DateField()
    tipr = models.DecimalField(max_digits=9, decimal_places=0)
    titp = models.CharField(max_length=10)
    tity = models.CharField(max_length=10)
    tino = models.BigIntegerField()
    sname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tick_mange'
        unique_together = (('tiid', 'sname'),)


class Train(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    type = models.CharField(max_length=20, blank=True, null=True)
    carriage_number = models.IntegerField(blank=True, null=True)
    station_departure = models.CharField(max_length=50, blank=True, null=True)
    station_arrival = models.CharField(max_length=50, blank=True, null=True)
    time_departure = models.DateTimeField(blank=True, null=True)
    time_arrival = models.DateTimeField(blank=True, null=True)
    time_consuming = models.CharField(max_length=50, blank=True, null=True)
    date_consuming = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    number1 = models.IntegerField(blank=True, null=True)
    number2 = models.IntegerField(blank=True, null=True)
    number3 = models.IntegerField(blank=True, null=True)
    box = models.IntegerField(blank=True, null=True)
    result = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'train'


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    card = models.CharField(max_length=50, blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    mail = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
