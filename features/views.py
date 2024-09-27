from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.db.models import Max
from django.template import loader
from .models import Members
from . import models
from .forms import Trsc,Usearch,AddR,AddSTform,AddTforms,AddRT
import json

from home.models import RouteStation,Station,Route,Trains,Reservation,Payment
def getTrains(request):
    if request.method=='POST':
        form=Usearch(request.POST)
        if form.is_valid():

            data=form.cleaned_data
            src=data['src']
            des=data['des']
            a=RouteStation.objects.filter(sid=des)
            x=[]
            o=0
            for i in a:
                tno=i.tno
                b=RouteStation.objects.filter(tno=tno,sid=src)
                for j in b:
                    if j.order<i.order:
                        x.append(j)
                        o=i.order-j.order

        else:
            return HttpResponse('<h1>invalid Data</h1>')
        return render(request,'features/trains.html',{'data':x,'o':o,'src':src,'des':des})
    return HttpResponse('<h1>Wrong REq</h1>')




def schedule(request):
    a=Trains.objects.all()
    return render(request,'features/schedule.html',{'a':a})

def getTinfo(request):
    form=Trsc(request.GET)
    if form.is_valid():
        data=form.cleaned_data
        tno=data['tnum']
        a=RouteStation.objects.filter(tno=tno).order_by('order')


        return render(request,'features/trinfo.html',{'data':a})

    return HttpResponse('<h1>DAta invalid<h1>')









def addR(request):
    if request.method == 'POST':
        form = AddR(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            a=Route()
            a.rid=data['rid']
            a.ostation=data['ostation']
            a.dstation=data['dstation']
            a.save()
            return redirect('/home/addR')
        else:
            return HttpResponse('<h1>Invalid Data</h1>')






    a=Station.objects.all()

    return render(request,'features/addR.html',{'stn':a})






def addRT(request):
    if request.method == 'POST':
        form = AddRT(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            a = RouteStation()
            t1= Trains.objects.get(tno=data['tno'])
            a.tno = t1
            s1=Station.objects.get(sid=data['sid'])
            a.sid = s1
            r1=Route.objects.get(rid=data['rid'])
            a.rid = r1
            a.order=data['order']
            a.atime=data['atime']
            a.save()
            return redirect('/home/addRT')
        else:
            return HttpResponse(form.errors)

    a = Route.objects.all()
    b=Trains.objects.all()
    c=Station.objects.all
    return render(request, 'features/addRT.html', {'rt': a,'tr':b,'st':c})


def cva(request):
    if request.method=='POST':
        tn1=request.POST['tno']
        o=int(request.POST['od'])

        cls=request.POST['cls']
        p=0
        if cls=='AC':
            p=120*o
        if cls=='SL':
            p=80*o
        if cls=='3A':
            p=100*o
        if cls=='2S':
            p=50*o
        dt=request.POST['dt']
        c=0
        a=Reservation.objects.filter(tno=tn1,cls=cls,date=dt)

        for i in a:
            c=c+i.nos
        if c>30:
            x="Waiting-"+str(c-30)
            data = json.dumps({
                'read': x,
                'price': p,
            })
            return HttpResponse(data,content_type='application/json')
        else:
            x="Available-"+str(30-c)
            data = json.dumps({
                'read': x,
                'price': p,
            })
            return HttpResponse(data,content_type='application/json')

def book1(request):
    if(request.method=='POST'):
        dt=request.POST['date']
        src=request.POST['src']
        des=request.POST['des']
        tno=request.POST['bk']
        cls = request.POST['cls'+str(tno)]
        nos=request.POST['nos'+str(tno)]
        pr=request.POST['price'+str(tno)]
        tname=Trains.objects.get(tno=tno).tname
        return render(request,'features/payment.html',{'price':int(pr)*int(nos),'dt':dt,'cls':cls,'tno':tno,'nos':nos,'tname':tname,'src':src,'des':des})


def book(request):

    if request.method=='POST':
        nos=int(request.POST['nos'])
        tno=request.POST['tno']
        dt=request.POST['date']
        tn1=Trains.objects.get(tno=tno)
        cls=request.POST['cls']
        op=request.POST['select']
        tname=request.POST['tname']
        src=request.POST['src']
        des=request.POST['des']
        price=int(request.POST['price'])
        pp=price/nos
        mtd='Paytm'
        if op=='option1':
            crd=request.POST['crd']
            nam=request.POST['nam']
            cvv=request.POST['cvv']
            exp=request.POST['exp']
            mtd='Credit/Debit Card'
            if len(crd)!=16 or len(cvv)!=3:
                return render(request,'features/nopay.html')


        c = 0
        f=0
        pay=Payment()
        pay.user=request.user
        pay.amt=price
        pay.date=dt
        pay.mtd=mtd
        pay.cancel='NO'

        a = Reservation.objects.filter(tno=tno, cls=cls, date=dt)
        c1=Reservation.objects.all()
        cp=0
        for i in c1:
            cp=max(cp,int(i.pnr))
        for i in a:
            c = c + i.nos
        if c<30:
            if nos>(30-c):
                b=Reservation()
                b.cls=cls
                b.tno=tn1
                b.status="C"
                b.nos=30-c
                b.amt=200
                b.date=dt
                b.user=request.user
                b.pnr=cp+1
                b.src=src
                b.des=des
                b.save()
                e = Reservation()
                e.cls = cls
                e.tno = tn1
                e.status = "W"
                e.nos = nos-(30 - c)
                e.amt = price
                e.date = dt
                e.user = request.user
                e.pnr = cp + 1
                e.src=src
                e.des=des
                e.save()
                f=1
            else:
                b = Reservation()
                b.cls = cls
                b.tno = tn1
                b.status = "C"
                b.nos = nos
                b.amt = price
                b.date = dt
                b.user = request.user
                b.pnr = cp + 1
                b.src=src
                b.des=des
                b.save()
                f = 1
        else:
            b = Reservation()
            b.cls = cls
            b.tno = tn1
            b.status = "W"
            b.nos = nos
            b.amt = price
            b.date = dt
            b.user = request.user
            b.pnr = cp + 1
            b.save()
            f=2
        c=0
        a = Reservation.objects.filter(tno=tno, cls=cls, date=dt)
        for i in a:
            c = c + i.nos

        pay.pnr = cp+1
        pay.save()
        return render(request,"features/final.html",{'tname':tname,'tno':tno,'date':dt,'src':src,'des':des,'cls':cls,'pnr':(cp+1),'nos':nos,'dt':dt})



def cancel(request):
    a=Reservation.objects.filter(user=request.user).values('pnr','date','tno','src','des','cls','nos').distinct()
    return render(request,'features/cancel.html',{'res':a})

def cn(request):

    if request.method=='POST':


        pnr=request.POST['id']
        a=Reservation.objects.filter(pnr=pnr)
        z=Payment.objects.filter(pnr=pnr,cancel='NO')
        for j in z:
            amt = j.amt
            j.cancel='YES'
            j.save()

        c=0
        cls='X'

        for i in a:
            if i.status=='C':
                c=c+i.nos
            cls=i.cls
        a.delete()
        a=Reservation.objects.all()
        f=0
        for i in a:
            if i.status=='W' and i.cls==cls:
                if i.nos<=c:
                    c=c-i.nos
                    i.status='C'
                    i.save()
                else:
                    f=1
                    b=Reservation()
                    b.cls = i.cls
                    b.tno = i.tno
                    b.status = "C"
                    b.nos = c
                    b.amt = 200
                    b.date = i.date
                    b.user = i.user
                    b.pnr = i.pnr
                    b.save()
                    i.nos=i.nos-c
                    i.save()
                    c=0
                    break
        return HttpResponse(amt)

def pnr(request):
    if request.method=='POST':
        pnr=request.POST['pnr']
        a=Reservation.objects.filter(pnr=pnr)

        return render(request,'features/pnr.html',{'r':a})


    return render(request,'features/pnr.html')





def addT(request):
    if request.method == 'POST':
        print(request.POST)
        form=models.Trainsmodel.objects.create(
            train_name=request.POST["train_name"],
            train_number=request.POST["train_number"],
            capacity=request.POST["capacity"],
        )

        form.save()
        return redirect('trains')
        # return render(request,'features/trinfo.html')
    return render(request,'features/addT.html')



def addST(request):
    if request.method == 'POST':
        stationform = AddSTform(request.POST)
        if stationform.is_valid():
            stationform.save()
            return redirect('/home/addST')
    return render(request, 'features/addST.html')



def schedule(request):
    a=models.Trainsmodel.objects.all()
    return render(request,'features/schedule.html',{'a':a})



def reservationview(request):
    if request.method =="POST":
        data=Members.objects.get(email=request.POST["email"])
        train=models.Trainsmodel.objects.get(train_name=request.POST["train_name"])
        shedule=models.schedulemodel.objects.get(train_name=request.POST["train_name"])
        form=models.Reservationmodel.objects.create(
            user=data,
            train=train,
            shedule=shedule,
            seat_reserved=request.POST["seat_reserved"],
            email=request.POST["email"],
            train_name=request.POST["train_name"],
            reservation_date = request.POST["reservation_date"],
            
        )
        form.save()
        return redirect('/home/addST')
    return render(request,'features/reservation.html')



def scheduleview(request):
    if request.method =="POST":
        data=models.stationmodel.objects.get(station_name=request.POST["station_name"])
        train=models.Trainsmodel.objects.get(train_name=request.POST["train_name"])
        form=models.schedulemodel.objects.create(
            train=train,
            station=data,
            train_name=request.POST["train_name"],
            station_name=request.POST["station_name"],
            departure_time=request.POST["departure_time"],
        )
        form.save()
        return redirect('/home/addST')
    return render(request,'features/scheduleadd.html')


def traindetails(request):
     data=models.schedulemodel.objects.all()
     return render(request,'features/trinfo.html',{"data":data})



def scheduledetails(request):
    data=models.schedulemodel.objects.all()
    return render(request,'features/trinfo.html',{"data":data})


def reservationdatas(request):
    reservedata=models.Reservationmodel.objects.all()
    return render(request,'features/cancel.html',{'reservedata':reservedata})

def reservecancel(request, id):
    reservation = get_object_or_404(models.Reservationmodel, reservastion_id=id)
    reservation.cancelstatus = True 
    reservation.save()
    return redirect("hom")



def searchtrain(request):
    alldata=models.schedulemodel.objects.all() 
    alltrains=models.Trainsmodel.objects.all()
    query = request.GET.get('q', '')  
    if query:
        alldata = models.schedulemodel.objects.filter(
            train_name__icontains=query
        ) | models.schedulemodel.objects.filter(
            station_name__icontains=query
        )
    context = {
        'all': alldata,
        'query': query,
        "alltrains":alltrains
    }
    return render(request,'features/seat.html',context)

def paymenttrain(request,train_id):
    data = models.Trainsmodel.objects.get(train_id=train_id)
    print(data)
    if request.method == "POST":
        
        paydata=models.paymentmodel.objects.create(
            train=data,
            from_station=request.POST["from_station"],
            to_station=request.POST["to_station"],
            trainclass=request.POST["trainclass"],
            no_seat=request.POST["no_seat"],
            card_number=request.POST['card_number'],
            nameon_card=request.POST["nameon_card"],
            cvvnumber=request.POST['cvvnumber'],
            expiry=request.POST['expiry'],
            
        )

        paydata.save()
        paydata=models.paymentmodel.objects.get(train__train_id=train_id)
        return render(request, 'features/final.html',{"paydata":paydata})
    return render(request,'features/payment.html',{"data":data})



def bookconfirm(request,train_id):
    data = models.paymentmodel.objects.get(train__train_id=train_id)
    return render(request, 'features/final.html',{"data":data})

