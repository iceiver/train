
from .serializers import *
from rest_framework.decorators import api_view
from .Action import Action



@api_view(['GET',"POST"])
def addSeat(request):
    train_id=request.POST.get('train_id')
    carriage_number=request.POST.get('carriage_number')
    type=request.POST.get('type')
    box=request.POST.get('box')
    boxs=Action.findSeatsByTrainId(train_id)
    for item_box in boxs:
        if item_box.box==box:
            return Action.fail("车厢编号重复")
    Action.createSeat(Action.check(train_id=train_id,carriage_number=carriage_number,type=type,box=box,))
    return Action.success()


@api_view(['GET',"POST"])
def editSeat(request):
    train_id=request.POST.get('train_id')
    id=request.POST.get('id')
    carriage_number=request.POST.get('carriage_number')
    type=request.POST.get('type')
    box=request.POST.get('box')
    Action.editSeat(id,Action.check(train_id=train_id,carriage_number=carriage_number,type=type,box=box,))
    return Action.success()


@api_view(['GET',"POST"])
def deleteSeat(request):
    id=request.POST.get('id')
    Action.deleteSeat(id)
    return Action.success()


@api_view(['GET',"POST"])
def findSeat(request):
    id=request.POST.get('id')
    return Action.success(SeatSerial(Action.findSeat(id)  ,many=False).data)


@api_view(['GET',"POST"])
def findSeats(request):

    train_id=request.POST.get("train_id")
    boxs=Action.findSeatsByTrainId(train_id)
    train_orders=Action.findOrdersByTrainId(train_id)
    for order in train_orders:
        if order.status=='3':
            continue
        for box in boxs:
            if box.box==order.box_name:
                box.count-=1
    return Action.success(SeatSerial(boxs  ,many=True).data)
    
    