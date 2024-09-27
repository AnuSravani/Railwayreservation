from django.urls import path
from django.contrib import admin
import home
from features import views
urlpatterns = [
    path('',home.views.home,name="hom" ),

    path('addT/',views.addT),
    path('addST/',views.addST),
    path('schedule/',views.schedule),
    path('reservationview/',views.reservationview),
    path('scheduleview/',views.scheduleview),
    path('traindetails',views.traindetails,name="trains"),
    # path('reservationdetails',views.reservationdetails,name="reser-data"),
    path('searchtrain/',views.searchtrain,name='searchtrain'),
    path('paymenttrain/<train_id>',views.paymenttrain,name='pay'),
    path('scheduledetails/',views.scheduledetails,name="shed"),
    path('reservationdatas/',views.reservationdatas,name="reservedetail"),
    path('reservecancel/<id>',views.reservecancel,name="cancel"),
    path('bookconfirm/<train_id>',views.bookconfirm,name="book"),

]