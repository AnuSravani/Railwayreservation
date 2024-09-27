from django.contrib import admin
from features.models import Members,Trainsmodel,stationmodel,schedulemodel,Reservationmodel

# Register your models here.
admin.site.register(Members)
admin.site.register(Trainsmodel)
admin.site.register(stationmodel)
admin.site.register(schedulemodel)
admin.site.register(Reservationmodel)