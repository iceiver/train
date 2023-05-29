from .models import *
import datetime
from django.http import JsonResponse
from django.utils import timezone
class Action:
    def __init__(self):
        pass

    @staticmethod
    def currentTime():
        return timezone.now()

    def consuming(t1,t2):
        if not type(t1) ==datetime.datetime:
            t1 = timezone.datetime.strptime(t1, '%Y-%m-%d %H:%M:%S')
        if not type(t2)==datetime.datetime:
            t2 = timezone.datetime.strptime(t2, '%Y-%m-%d %H:%M:%S')
        ts=abs((t1-t2).total_seconds())
        h=int(ts/3600)
        m=int(ts%3600/60)
        s=int(ts%60)
        return str(h)+"小时"+str(m)+"分钟"+str(s)+"秒"
    def dayconsuming(t1,t2):
        t1=str(t1)[:18]
        t2=str(t2)[:18]
        t1 = timezone.datetime.strptime(t1, '%Y-%m-%d %H:%M:%S')
        t2 = timezone.datetime.strptime(t2, '%Y-%m-%d %H:%M:%S')
        ts=abs((t1-t2).days)
        if ts=='0':
            return  '当日'
        elif ts=='1':
            return '次日'
        else:
            return str(ts)+"日"

    @staticmethod
    def check(**kwargss):
        return {k: v for k, v in kwargss.items() if v and v != 'null'}

    @staticmethod
    def success(data=""):
        return JsonResponse({"code": 200, "data": data}, safe=False)

    @staticmethod
    def fail(data=""):
        return JsonResponse({"code": 500, "data": data}, safe=False)

    # Order

    @staticmethod
    def createOrder(kwargss):
        return Order.objects.create(**kwargss)

    @staticmethod
    def editOrder(id, kwargs):
        Order.objects.filter(id=id).update(**kwargs)

    @staticmethod
    def findOrders():
        return Order.objects.all()

    @staticmethod
    def findOrder(id):
        return Order.objects.get(id=id)

    @staticmethod
    def deleteOrder(id):
        return Order.objects.get(id=id).delete()

    # Passby

    @staticmethod
    def createPassby(kwargss):
        print(kwargss)
        ps = Passby.objects.filter(train_id=kwargss['train_id'])
        if not ps:
            kwargss['root'] = 1
            return Passby.objects.create(**kwargss)
        p = Passby.objects.create(**kwargss)
        id=""
        for i in ps:
            if not i.next_id:
                i.next_id = p.id
                i.save()
                return p


    @staticmethod
    def editPassby(id, kwargs):
        print(kwargs)
        Passby.objects.filter(id=id).update(**kwargs)


    @staticmethod
    def findPassbys():
        return Passby.objects.all()


    @staticmethod
    def findPassby(id):
        return Passby.objects.get(id=id)


    @staticmethod
    def deletePassby(id):
        p=Passby.objects.filter(next_id=id)
        d=Passby.objects.get(id=id)
        if p:
            p=p.first()
            p.next_id=d.next_id
            p.save()
        if d.root==1 and d.next_id:
            r=Passby.objects.get(id=d.next_id);
            r.root=1
            r.save()
        return d.delete()



    # Seat

    @staticmethod
    def createSeat(kwargss):
        t=Train.objects.get(id=kwargss['train_id'])
        if not t.carriage_number:
            t.carriage_number=0
        t.carriage_number=t.carriage_number+int(kwargss['carriage_number'])
        kwargss['count']=kwargss['carriage_number']
        t.save()
        return Seat.objects.create(**kwargss)


    @staticmethod
    def editSeat(id, kwargs):
        kwargs['count']=kwargs['carriage_number']
        Seat.objects.filter(id=id).update(**kwargs)
        s=Seat.objects.filter(train_id=kwargs['train_id'])
        n=0
        for i in s:
            n+=i.carriage_number
        Train.objects.filter(id=kwargs['train_id']).update(carriage_number=n)

    @staticmethod
    def findSeats():
        return Seat.objects.all()


    @staticmethod
    def findSeat(id):
        return Seat.objects.get(id=id)


    @staticmethod
    def deleteSeat(id):
        s=Seat.objects.get(id=id)
        t=Train.objects.get(id=s.train_id)
        t.carriage_number=t.carriage_number-s.carriage_number
        t.save()
        return s.delete()


    # Staff

    @staticmethod
    def loginStaff(sname, password):
        return Staff.objects.get(sname=sname, password=password)

    @staticmethod
    def createStaff(kwargss):
        return Staff.objects.create(**kwargss)


    @staticmethod
    def editStaff(id, kwargs):
        Staff.objects.filter(id=id).update(**kwargs)


    @staticmethod
    def findStaffs():
        return Staff.objects.all()


    @staticmethod
    def findStaff(sname):
        return Staff.objects.get(sname=sname)


    @staticmethod
    def deleteStaff(id):
        return Staff.objects.get(id=id).delete()



    # Train

    @staticmethod
    def createTrain(kwargss):
        kwargss['time_consuming']=Action.consuming(kwargss['time_departure'],kwargss['time_arrival'])
        kwargss['date_consuming']=Action.dayconsuming(kwargss['time_departure'],kwargss['time_arrival'])

        return Train.objects.create(**kwargss)


    @staticmethod
    def editTrain(id, kwargs):
        kwargs['time_consuming']=Action.consuming(kwargs['time_departure'],kwargs['time_arrival'])
        kwargs['date_consuming']=Action.dayconsuming(kwargs['time_departure'],kwargs['time_arrival'])
        Train.objects.filter(id=id).update(**kwargs)


    @staticmethod
    def findTrains():
        return Train.objects.all()


    @staticmethod
    def findTrain(id):
        return Train.objects.get(id=id)

    @staticmethod
    def findTrainFromTo(station_departure, station_arrival):
        if (station_departure and station_arrival):
            print(1)
            return Train.objects.filter(station_departure__icontains=station_departure, station_arrival__icontains=station_arrival)
        elif station_departure:
            print(2)
            return Train.objects.filter(station_departure__icontains=station_departure)
        elif station_arrival:
            print(3)
            return Train.objects.filter(station_arrival__icontains=station_arrival)
        else:
            return Train.objects.all()


    @staticmethod
    def deleteTrain(id):
        return Train.objects.get(id=id).delete()


    # User

    @staticmethod
    def createUser(kwargss):
        return User.objects.create(**kwargss)


    @staticmethod
    def editUser(id, kwargs):
        User.objects.filter(id=id).update(**kwargs)


    @staticmethod
    def findUsers():
        return User.objects.all()


    @staticmethod
    def loginUser(name, password):
        return User.objects.get(name=name, password=password)

    @staticmethod
    def findUser(name):
        return User.objects.get(name=name)

    @staticmethod
    def findUsersWithName(name):
        return User.objects.filter(name=name)

    @staticmethod
    def deleteUser(id):
        return User.objects.get(id=id).delete()


    @staticmethod
    def findSeatsByTrainId(id):
        return Seat.objects.filter(train_id=id)


    @staticmethod
    def findPassbysById(id):
        return Passby.objects.filter(train_id=id)

    @staticmethod
    def trainGo(id):
        # allp=Passby.objects.filter(train_id=id)
        # if not allp:
        #     return Action.fail("没有站点")
        # 获取火车
        t=Train.objects.get(id=id)
        # allp.update(arrival_time=None,start_time=None,time_consuming=None,current=0,arrive=0)
        c=Action.currentTime()
        # p=Passby.objects.filter(train_id=id,root=1).update(arrival_time=c,start_time=c,time_consuming=0,current=1,arrive=1)
        # pp=Passby.objects.get(train_id=id,root=1)
        # if not pp.next_id:
            # return Action.trainEnd(id)
        # Passby.objects.filter(id=pp.next_id).update(start_time=c)
        t.status='出行中'
        t.save()
        return Action.success("")
    @staticmethod
    def trainEnd(id):
        print("-----------调用end------------")
        # 列车结束时候  车厢的容量为最大值
        s=Seat.objects.all()
        for i in s:
            i.count=i.carriage_number
            i.save()


        t=Train.objects.get(id=id)
        t.status="空闲"
        t.save()
        return Action.success("出行完毕")
    @staticmethod
    def checkTrainStart(id):
        t=Train.objects.get(id=id)
        if t.status=='出行中':
            return True

    @staticmethod
    def trainNext(train_id):
        if not Action.checkTrainStart(train_id):
            return Action.fail("列出没有出行")
        remind=Passby.objects.filter(train_id=train_id,current=1).first()

        #到达站点完成订单
        Order.objects.filter(train_id=train_id,to=remind.station_id,status=2).update(status=1)
        if not remind or remind==None:
            return Action.trainEnd(train_id)
        c=Action.currentTime()
        print(remind.start_time)
        print(remind)
        remind.time_consuming=Action.consuming(c,remind.start_time)
        remind.arrival_time=c
        remind.arrive=1
        remind.current=0
        remind.save()
        if not remind.next_id:
            return Action.trainEnd(train_id)
        next_=Passby.objects.get(id=remind.next_id)
        next_.current=1
        next_.start_time=c
        next_.save()
        return Action.success()

    @staticmethod
    def findOrdersById( user_id):
        return Order.objects.filter(user_id=user_id)
    @staticmethod
    def findOrdersByTrainId(train_id):
        return Order.objects.filter(train_id=train_id)

