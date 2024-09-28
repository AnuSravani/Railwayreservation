from django.contrib import admin
from features.models import Members,Trainsmodel,stationmodel,schedulemodel,Reservationmodel,paymentmodel

# Register your models here.
admin.site.register(Members)
admin.site.register(Trainsmodel)
admin.site.register(stationmodel)
admin.site.register(schedulemodel)
admin.site.register(Reservationmodel)

admin.site.register(paymentmodel)
