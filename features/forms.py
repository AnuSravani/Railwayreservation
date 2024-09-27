from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from features.models import Trainsmodel,stationmodel,Reservationmodel,schedulemodel

class Usearch(forms.Form):
    src=forms.CharField(max_length=50)
    des = forms.CharField(max_length=50)

class Trsc (forms.Form):
    tnum=forms.IntegerField()

class AddR(forms.Form):
    rid=forms.CharField(max_length=50)
    ostation=forms.CharField(max_length=50)
    dstation=forms.CharField(max_length=50)

class AddSTform(forms.ModelForm):
    class Meta:
        model=stationmodel
        fields=["station_name","location"]



class AddTforms(forms.ModelForm):
    class Meta:
        model=Trainsmodel
        fields=["train_name","train_number","capacity"]

        
# class Addreservationform(forms.ModelForm):
#     class Meta:
#         model=Reservationmodel
#         fields=["user","shedule","seat_reserved"]


# class scheduleform(forms.ModelForm):
#     class Meta:
#         model=schedulemodel
#         fields=["train","station","email","train_name"]




class AddRT(forms.Form):
    tno=forms.CharField(max_length=50)
    sid= forms.CharField(max_length=50)
    rid=forms.CharField(max_length=50)
    order=forms.IntegerField()
    atime=forms.CharField(max_length=50)

class Pnr(forms.Form):
    pnr=forms.CharField(max_length=50)

class Book(forms.Form):
    cls=forms.CharField(max_length=10)
    dt=forms.CharField(max_length=10)
