
from .serializers import *
from rest_framework.decorators import api_view
from .Action import Action



@api_view(['GET',"POST"])
def addRefund(request):
    tiid=request.POST.get('tiid')
    slid=request.POST.get('slid')
    returnprice=request.POST.get('returnprice')
    Action.createRefund(Action.check(tiid=tiid,slid=slid,returnprice=returnprice,))
    return Action.success()



@api_view(['GET',"POST"])
def editRefund(request):
    tiid=request.POST.get('tiid')
    slid=request.POST.get('slid')
    returnprice=request.POST.get('returnprice')
    Action.createRefund(Action.check(tiid=tiid,slid=slid,returnprice=returnprice,))
    return Action.success()



@api_view(['GET',"POST"])
def deleteRefund(request):
    id=request.POST.get('train_id')
    Action.deleteRefund(id)
    return Action.success()


@api_view(['GET',"POST"])
def findRefund(request):
    id=request.POST.get('id')
    return Action.success(RefundSerial(Action.findRefund(id)  ,many=False).data)


@api_view(['GET',"POST"])
def findRefunds(request):

    user_id=request.POST.get("train_id")
    if user_id:
        orders=Action.findRefundsById(user_id)
    else:
        orders=Action.findRefunds()
    return Action.success(RefundSerial(orders  ,many=True).data)
    
    