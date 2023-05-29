
from .serializers import *
from rest_framework.decorators import api_view
from .Action import Action



@api_view(['GET',"POST"])
def loginUser(request):
    name=request.POST.get('name')
    password=request.POST.get('password')
    return Action.success(UserSerial(Action.loginUser(name, password),many=False).data)

@api_view(['GET',"POST"])
def addUser(request):
    name=request.POST.get('name')
    sex=request.POST.get('sex')
    card=request.POST.get('card')
    phone=request.POST.get('phone')
    mail=request.POST.get('mail')
    address=request.POST.get('address')
    password=request.POST.get('password')
    if not name or not card or not phone :
        return Action.fail("缺少字段")
    users=Action.findUsersWithName(name)
    if len(users) > 0:
        return Action.fail("姓名重复")
    Action.createUser(Action.check(name=name,sex=sex,card=card,phone=phone,mail=mail,address=address,password=password))
    return Action.success()



@api_view(['GET',"POST"])
def editUser(request):
    id=request.POST.get('id')
    name=request.POST.get('name')
    sex=request.POST.get('sex')
    card=request.POST.get('card')
    phone=request.POST.get('phone')
    mail=request.POST.get('mail')
    address=request.POST.get('address')
    password=request.POST.get('password')
    Action.editUser(id,Action.check(name=name,sex=sex,card=card,phone=phone,mail=mail,address=address,password=password))
    return Action.success()



@api_view(['GET',"POST"])
def deleteUser(request):
    id=request.POST.get('id')
    Action.deleteUser(id)
    return Action.success()


@api_view(['GET',"POST"])
def findUser(request):
    name=request.POST.get('name')
    return Action.success(UserSerial(Action.findUser(name),many=False).data)


@api_view(['GET',"POST"])
def findUsers(request):
    # user_id=request.POST.get("train_id")
    # if user_id:
    #     orders=Action.findUsersById(user_id)
    # else:
    orders=Action.findUsers()
    return Action.success(UserSerial(orders  ,many=True).data)
    
    