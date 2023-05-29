from django.urls import path
from . import views,view_Train,view_Order,view_Passby,view_Refund,view_Seat,view_Staff,view_User,view_Logic


urlpatterns = [
    path("ad",views.ad,name="ad"),
    path("us",views.us,name="us"),
    path("home",views.home,name="home"),


    path("addOrder",view_Order.addOrder,name="addOrder"),
    path("editOrder",view_Order.editOrder,name="editOrder"),
    path("orderChangeTicket",view_Order.orderChangeTicket,name="orderChangeTicket"),
    path("deleteOrder",view_Order.deleteOrder,name="deleteOrder"),
    path("findOrder",view_Order.findOrder,name="findOrder"),
    path("findOrders",view_Order.findOrders,name="findOrders"),
    path("orderRefund",view_Order.orderRefund,name="orderRefund"),



    path("addPassby",view_Passby.addPassby,name="addPassby"),
    path("editPassby",view_Passby.editPassby,name="editPassby"),
    path("deletePassby",view_Passby.deletePassby,name="deletePassby"),
    path("findPassby",view_Passby.findPassby,name="findPassby"),
    path("findPassbys",view_Passby.findPassbys,name="findPassbys"),




    path("addRefund",view_Refund.addRefund,name="addRefund"),
    path("editRefund",view_Refund.editRefund,name="editRefund"),
    path("deleteRefund",view_Refund.deleteRefund,name="deleteRefund"),
    path("findRefund",view_Refund.findRefund,name="findRefund"),
    path("findRefunds",view_Refund.findRefunds,name="findRefunds"),



    path("addSeat",view_Seat.addSeat,name="addSeat"),
    path("editSeat",view_Seat.editSeat,name="editSeat"),
    path("deleteSeat",view_Seat.deleteSeat,name="deleteSeat"),
    path("findSeat",view_Seat.findSeat,name="findSeat"),
    path("findSeats",view_Seat.findSeats,name="findSeats"),



    path("loginStaff",view_Staff.loginStaff,name="loginStaff"),
    path("addStaff",view_Staff.addStaff,name="addStaff"),
    path("editStaff",view_Staff.editStaff,name="editStaff"),
    path("deleteStaff",view_Staff.deleteStaff,name="deleteStaff"),
    path("findStaff",view_Staff.findStaff,name="findStaff"),
    path("findStaffs",view_Staff.findStaffs,name="findStaffs"),



    path("addTrain",view_Train.addTrain,name="addTrain"),
    path("editTrain",view_Train.editTrain,name="editTrain"),
    path("deleteTrain",view_Train.deleteTrain,name="deleteTrain"),
    path("findTrain",view_Train.findTrain,name="findTrain"),
    path("findTrains",view_Train.findTrains,name="findTrains"),
    path("findTrainFromTo",view_Train.findTrainFromTo,name="findTrainFromTo"),



    path("loginUser",view_User.loginUser,name="loginUser"),
    path("addUser",view_User.addUser,name="addUser"),
    path("editUser",view_User.editUser,name="editUser"),
    path("deleteUser",view_User.deleteUser,name="deleteUser"),
    path("findUser",view_User.findUser,name="findUser"),
    path("findUsers",view_User.findUsers,name="findUsers"),


    path("trainGo",view_Logic.trainGo,name="trainGo"),
    path("trainNext",view_Logic.trainNext,name="trainNext"),
    path("findTo",view_Logic.findTo,name="findTo"),
    path("findByFromTo",view_Logic.findByFromTo,name="findByFromTo"),


]