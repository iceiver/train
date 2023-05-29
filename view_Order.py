
from .serializers import *
from rest_framework.decorators import api_view
from .Action import Action

@api_view(['GET',"POST"])
def addOrder(request):
    train_id=request.POST.get('id')
    status='2'
    from_field=request.POST.get('station_departure')
    to=request.POST.get('station_arrival')
    user_id=request.POST.get('user_id')
    user_name=request.POST.get('name')
    user_card=request.POST.get('card')
    box=request.POST.get('box')
    # 获取该列车的所有订单
    train_orders=Action.findOrdersByTrainId(train_id)
    seat_id = 1
    for order in train_orders:
        if order.status=='3':
            continue
        if user_id==str(order.user_id) :
            return Action.fail("不可重复购票")
        order_seat_id = order.seat_id
        order_box_name = order.box_name
        if order_box_name==box :
            if order_seat_id==seat_id :
                seat_id += 1
    seat_name=box+"厢"+str(seat_id)+"号"
    Action.createOrder(Action.check(box_name=box,seat_name=seat_name,train_id=train_id,status=status,from_field=from_field,to=to,user_id=user_id,user_name=user_name,user_card=user_card,seat_id=seat_id,))
    return Action.success()

@api_view(['GET',"POST"])
def editOrder(request):
    id=request.POST.get('id')
    train_id=request.POST.get('id')
    status='2'
    from_field=request.POST.get('station_departure')
    to=request.POST.get('station_arrival')
    user_id=request.POST.get('user_id')
    user_name=request.POST.get('name')
    user_card=request.POST.get('card')
    seat_id=request.POST.get('seat_id')
    box=request.POST.get('box')
    seat_name=box+"厢"+seat_id+"号"
    Action.createOrder(Action.check(seat_name=seat_name,id=id,train_id=train_id,status=status,from_field=from_field,to=to,user_id=user_id,user_name=user_name,user_card=user_card,seat_id=seat_id,))
    return Action.success()

@api_view(['GET',"POST"])
def orderChangeTicket(request):
    train_id=request.POST.get('train_id')
    user_id=request.POST.get('user_id')
    order_id=request.POST.get('order_id')
    from_field=request.POST.get('station_departure')
    to=request.POST.get('station_arrival')
    boxs=Action.findSeatsByTrainId(train_id)
    train_orders=Action.findOrdersByTrainId(train_id)
    if len(boxs)==0:
        return Action.fail("已售罄")
    box_name=boxs[0].box
    seat_id=1
    for box in boxs:
        for order in train_orders:
            if order.box_name==box.box and order.status!='3':
                box.count-=1
        if box.count>0:
            box_name = box.box
            for order in train_orders:
                if user_id==str(order.user_id) and order.status!='3':
                    return Action.fail("不可重复购票")
                order_seat_id = order.seat_id
                order_box_name = order.box_name
                if order_box_name==box and order.status!='3':
                    if order_seat_id==seat_id :
                        seat_id += 1
    seat_name=box_name+"厢"+str(seat_id)+"号"
    Action.editOrder(str(order_id),Action.check(box_name=box_name,id=str(order_id),train_id=train_id,status='4',from_field=from_field,to=to,seat_id=str(seat_id), seat_name=seat_name))
    return Action.success()


@api_view(['GET',"POST"])
def deleteOrder(request):
    id=request.POST.get('train_id')
    Action.deleteOrder(id)
    return Action.success()


@api_view(['GET',"POST"])
def findOrder(request):
    id=request.POST.get('id')
    return Action.success(OrderSerial(Action.findOrder(id)  ,many=False).data)


@api_view(['GET',"POST"])
def findOrders(request):
    user_id=request.POST.get("user_id")
    if user_id:
        orders=Action.findOrdersById(user_id)
    else:
        orders=Action.findOrders()
    return Action.success(OrderSerial(orders  ,many=True).data)
    
def orderRefund(reqest):
    id=reqest.POST.get("id")
    o=Order.objects.get(id=id)
    o.status=3
    o.save()
    return Action.success()
