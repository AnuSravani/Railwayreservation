from django.db import models
import string
import random

# Create your models here.
class Members(models.Model): 
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=16)
    email=models.CharField(max_length=250)
    number=models.CharField(max_length=10)

def generate_train_id(length=8):
    characters = string.ascii_uppercase + string.digits
    uid = ''.join(random.choice(characters) for _ in range(length))
    return uid

class Trainsmodel(models.Model):
    train_id=models.TextField()
    train_name = models.TextField()
    train_number = models.TextField()
    capacity= models.TextField()
    def save(self, *args, **kwargs):
        if not self.train_id:  # Only generate a new ID if it doesn't exist
            self.train_id = generate_train_id()
        super(Trainsmodel, self).save(*args, **kwargs)


def generate_station_id(length=8):
    characters = string.ascii_uppercase + string.digits
    uid = ''.join(random.choice(characters) for _ in range(length))
    return uid
class stationmodel(models.Model):
    station_id=models.TextField()
    station_name=models.TextField()
    location = models.TextField()
    def save(self, *args, **kwargs):
        if not self.station_id:  # Only generate a new ID if it doesn't exist
            self.station_id = generate_station_id()
        super(stationmodel, self).save(*args, **kwargs)



def generate_schedule_id(length=8):
    characters = string.ascii_uppercase + string.digits
    uid = ''.join(random.choice(characters) for _ in range(length))
    return uid
class schedulemodel(models.Model):
    schedule_id=models.TextField()
    train=models.ForeignKey(Trainsmodel,on_delete=models.CASCADE)
    station=models.ForeignKey(stationmodel,on_delete=models.CASCADE)
    arrival_time=models.TimeField(auto_now_add=True)
    departure_time=models.TimeField(null=True)
    schdule_date= models.DateField(auto_now_add=True)
    train_name=models.TextField(null=True)

    station_name=models.TextField(null=True)

    def save(self, *args, **kwargs):
        if not self.schedule_id:  # Only generate a new ID if it doesn't exist
            self.schedule_id = generate_schedule_id()
        super(schedulemodel, self).save(*args, **kwargs)



def generate_reservastion_id(length=8):
    characters = string.ascii_uppercase + string.digits
    uid = ''.join(random.choice(characters) for _ in range(length))
    return uid
class Reservationmodel(models.Model):

    reservastion_id=models.TextField()
    user=models.ForeignKey(Members,on_delete=models.CASCADE)
    train=models.ForeignKey(Trainsmodel,on_delete=models.CASCADE,null=True)
    shedule=models.ForeignKey(schedulemodel,on_delete=models.CASCADE,null=True)
    reservation_date= models.DateField(null=True)
    seat_reserved= models.TextField()
    email = models.EmailField(null=True)
    train_name=models.TextField(null=True)
    cancelstatus=models.BooleanField(default=False,null=True)
  
    def save(self, *args, **kwargs):
        if not self.reservastion_id:  # Only generate a new ID if it doesn't exist
            self.reservastion_id = generate_reservastion_id()
        super(Reservationmodel, self).save(*args, **kwargs)



class paymentmodel(models.Model):
    train=models.ForeignKey(Trainsmodel,on_delete=models.CASCADE)
    from_station=models.TextField()
    to_station=models.TextField()
    trainclass=models.TextField()
    no_seat=models.TextField()
    date=models.DateField(auto_now_add=True)
    card_number=models.TextField()
    nameon_card=models.TextField()
    cvvnumber=models.TextField()
    expiry=models.DateField()