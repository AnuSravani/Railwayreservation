from django.contrib import admin
from django.urls import path,include
import features
import features.views
from . import views
app_name='home'
urlpatterns = [
    path('',views.home,name="hom" ),
    path('logout/',views.logout ),
    # path('search/',features.views.search),
    path('search/trains',features.views.getTrains),
    path('schedule/',features.views.schedule),
    path('schedule/trains',features.views.getTinfo),
    path('addR/',features.views.addR,name="addR"),
    path('addST/',features.views.addST),
    path('addT/',features.views.addT),
    path('addRT/',features.views.addRT),
    path('search/search/trains/cva/', features.views.cva),
    path('search/book1/', features.views.book1),
    path('search/book1/book/', features.views.book),
    path('cancel/',features.views.cancel),
    path('cancel/cancel/cn/',features.views.cn),
    path('pnr/',features.views.pnr,name="pnr"),
    path('reservationview/',features.views.reservationview,name="reserve"),
    path('scheduleview/',features.views.scheduleview),

    path('traindetails/',features.views.traindetails,name="trains"),
    # path('reservationdetails/',features.views.reservationdetails,name="reserve-data"),
    path('searchtrain/',features.views.searchtrain,name='searchtrain'),
    path('paymenttrain/<train_id>',features.views.paymenttrain,name="pay"),
    path('scheduledetails/',features.views.scheduledetails,name="shed"),
    path('reservationdatas/',features.views.reservationdatas,name="reservedetail"),
    path('reservecancel/<id>',features.views.reservecancel,name="cancel"),
    path('bookconfirm/<train_id>',features.views.bookconfirm,name="book"),





    ]