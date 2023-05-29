from rest_framework import serializers
from train.models import *

class OrderSerial(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
              'id',
              'train_id',
              'create_time',
              'status',
              'from_field',
              'to',
              'user_id',
              'user_name',
              'user_card',
              'seat_id',
              'seat_name',
                'user_phone',
            # 'train_departure'
              )
class PassbySerial(serializers.ModelSerializer):
    class Meta:
        model = Passby
        fields = (
              'train_id',
              'station_id',
              'arrival_time',
              'start_time',
              'arrival_tim',
              'start_tim',
              'time_consuming',
              'root',
              'next_id',
              'arrive',
            'id',
            'current'
              )
class PassengerSerial(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = (
              'name',
              'gender',
              'tel',
              'address',
              'type',
              )
class RefundSerial(serializers.ModelSerializer):
    class Meta:
        model = Refund
        fields = (
              'tiid',
              'slid',
              'returnprice',
              )
class SeatSerial(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = (
              'train_id',
              'carriage_number',
              'type',
              'box',
            'count',
            'id',
              )
class StaffSerial(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = (
              'slid',
              'slna',
              'slpa',
              'sname',
              'password',
              )
class StationSerial(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = (
              'sname',
              'scna',
              'spr',
              'slid',
              'id',
              )
class TickMangeSerial(serializers.ModelSerializer):
    class Meta:
        model = TickMange
        fields = (
              'tiid',
              'tiss',
              'tias',
              'tist',
              'tiat',
              'tipr',
              'titp',
              'tity',
              'tino',
              'sname',
              )
class TrainSerial(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = (
              'id',
              'type',
              'carriage_number',
              'station_departure',
              'station_arrival',
              'time_departure',
              'time_arrival',
              'time_consuming',
              'date_consuming',
              'status',
              'number1',
              'number2',
              'number3',
              'box',
              )
class UserSerial(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
              'id',
              'name',
              'sex',
              'card',
              'phone',
              'mail',
              'address',
              'password'
              )
