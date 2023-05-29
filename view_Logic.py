from django.http import JsonResponse
from .serializers import *
from rest_framework.decorators import api_view
from .Action import Action
from .models import  *



@api_view(['GET',"POST"])
def addPassenger(request):
    id=request.POST.get('id')
    return Action.success(OrderSerial(Action.findOrder(id)  ,many=False).data)

def trainGo(request):
    id=request.POST.get('id')
    return  Action.trainGo(id)

def trainNext(request):
    train_id=request.POST.get('train_id')
    return Action.trainNext(train_id)


def findTo(request):
    train_id=request.POST.get('train_id')
    return Action.trainNext(train_id)


def findByFromTo(request):
    from_=request.POST.get('from')
    to=request.POST.get('to')
    id=request.POST.get('id')
    p1=Passby.objects.filter(station_id=from_,train_id=id).first()
    p2=Passby.objects.filter(station_id=to,train_id=id).first()
    t=TrainSerial(Train.objects.get(id=id),many=False).data
    print(p1.start_tim)
    print(p2.start_tim)
    time=Action.consuming(p1.start_tim,p2.start_tim)
    t['start_tim']=p1.start_tim
    t['arrival_tim']=p2.start_tim
    t['time_consuming']=time
    return JsonResponse({"code": 200, "data": t}, safe=False)


