
from .serializers import *
from rest_framework.decorators import api_view
from .Action import Action


@api_view(['GET',"POST"])
def loginStaff(request):
    sname=request.POST.get('sname')
    password=request.POST.get('password')
    return Action.success(StaffSerial(Action.loginStaff(sname, password),many=False).data)

@api_view(['GET',"POST"])
def addStaff(request):
    slid=request.POST.get('slid')
    slna=request.POST.get('slna')
    slpa=request.POST.get('slpa')
    sname=request.POST.get('sname')
    Action.createStaff(Action.check(slid=slid,slna=slna,slpa=slpa,sname=sname,))
    return Action.success()



@api_view(['GET',"POST"])
def editStaff(request):
    slid=request.POST.get('slid')
    slna=request.POST.get('slna')
    slpa=request.POST.get('slpa')
    sname=request.POST.get('sname')
    Action.createStaff(Action.check(slid=slid,slna=slna,slpa=slpa,sname=sname,))
    return Action.success()



@api_view(['GET',"POST"])
def deleteStaff(request):
    id=request.POST.get('train_id')
    Action.deleteStaff(id)
    return Action.success()


@api_view(['GET',"POST"])
def findStaff(request):
    sname=request.POST.get('sname')
    return Action.success(StaffSerial(Action.findStaff(sname)  ,many=False).data)


@api_view(['GET',"POST"])
def findStaffs(request):

    user_id=request.POST.get("train_id")
    if user_id:
        orders=Action.findStaffsById(user_id)
    else:
        orders=Action.findStaffs()
    return Action.success(StaffSerial(orders  ,many=True).data)
    
    