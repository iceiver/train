
from .serializers import *
from rest_framework.decorators import api_view
from .Action import Action



@api_view(['GET',"POST"])
def addPassby(request):
    train_id=request.POST.get('train_id')
    station_id=request.POST.get('station_id')
    arrival_tim=request.POST.get('arrival_tim')
    start_tim=request.POST.get('start_tim')
    Action.createPassby(Action.check(train_id=train_id,station_id=station_id,start_tim=start_tim,arrival_tim=arrival_tim))
    return Action.success()



@api_view(['GET',"POST"])
def editPassby(request):
    id=request.POST.get('id')
    station_id=request.POST.get('station_id')
    arrival_tim=request.POST.get('arrival_tim')
    start_tim=request.POST.get('start_tim')
    Action.editPassby(id,Action.check(station_id=station_id,start_tim=start_tim,arrival_tim=arrival_tim))
    return Action.success()



@api_view(['GET',"POST"])
def deletePassby(request):
    id=request.POST.get('id')
    Action.deletePassby(id)
    return Action.success()


@api_view(['GET',"POST"])
def findPassby(request):
    id=request.POST.get('id')
    return Action.success(PassbySerial(Action.findPassby(id)  ,many=False).data)


@api_view(['GET',"POST"])
def findPassbys(request):

    user_id=request.POST.get("train_id")
    if user_id:
        orders=Action.findPassbysById(user_id)
    else:
        orders=Action.findPassbys()
    return Action.success(PassbySerial(orders  ,many=True).data)
    
    