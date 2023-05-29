
from .serializers import *
from rest_framework.decorators import api_view
from .Action import Action
import time



@api_view(['GET',"POST"])
def addTrain(request):
    id=request.POST.get('id')
    type=request.POST.get('type')
    carriage_number= 0
    station_departure=request.POST.get('station_departure')
    station_arrival=request.POST.get('station_arrival')
    time_departure=request.POST.get('time_departure')
    time_arrival=request.POST.get('time_arrival')
    time_consuming=request.POST.get('time_consuming')
    date_consuming=request.POST.get('date_consuming')
    status='空闲'
    number1=0
    number2=0
    number3=0
    box=request.POST.get('box')
    Action.createTrain(Action.check(id=id,type=type,carriage_number=carriage_number,station_departure=station_departure,station_arrival=station_arrival,time_departure=time_departure,time_arrival=time_arrival,time_consuming=time_consuming,date_consuming=date_consuming,status=status,number1=number1,number2=number2,number3=number3,box=box,))
    return Action.success()



@api_view(['GET',"POST"])
def editTrain(request):
    old_id=request.POST.get('old_id')
    id=request.POST.get('id')
    type=request.POST.get('type')
    carriage_number=request.POST.get('carriage_number')
    station_departure=request.POST.get('station_departure')
    station_arrival=request.POST.get('station_arrival')
    time_departure=request.POST.get('time_departure')
    time_arrival=request.POST.get('time_arrival')
    time_consuming=request.POST.get('time_consuming')
    date_consuming=request.POST.get('date_consuming')


    status=request.POST.get('status')
    number1=request.POST.get('number1')
    number2=request.POST.get('number2')
    number3=request.POST.get('number3')
    box=request.POST.get('box')
    Action.editTrain(old_id,Action.check(id=id,type=type,carriage_number=carriage_number,station_departure=station_departure,station_arrival=station_arrival,time_departure=time_departure,time_arrival=time_arrival,time_consuming=time_consuming,date_consuming=date_consuming,status=status,number1=number1,number2=number2,number3=number3,box=box,))
    return Action.success()


@api_view(['GET',"POST"])
def deleteTrain(request):
    id=request.POST.get('id')
    Action.deleteTrain(id)
    return Action.success()


@api_view(['GET',"POST"])
def findTrain(request):
    id=request.POST.get('id')
    trains=TrainSerial(Action.findTrain(id),many=False).data
    for train in trains:
        train.time_departure=time.strftime("%Y-%m-%d %H:%M:%S", time.time(train.time_departure))
    # return Action.success(TrainSerial(Action.findTrain(id),many=False).data)
    return Action.success(trains)

@api_view(['GET',"POST"])
def findTrainFromTo(request):
    station_departure=request.POST.get('station_departure')
    station_arrival=request.POST.get('station_arrival')
    return Action.success(TrainSerial(Action.findTrainFromTo(station_departure, station_arrival)  ,many=True).data)


@api_view(['GET',"POST"])
def findTrains(request):
    trains=Action.findTrains()
    return Action.success(TrainSerial(trains  ,many=True).data)

