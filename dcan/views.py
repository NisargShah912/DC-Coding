from django.shortcuts import render
from django.conf import settings
from dcan.models import *
from qrcode import *
from django.contrib import messages
from django.shortcuts import redirect
log=False
def qr_gen(request):
    if log==True:
        if request.method == 'POST':
            data = request.POST['data']
            loc = request.POST['loc']
            ext = request.POST['ext']
            dat="D:/WEBSITES/DC-Django/dcanimal/templates/"+str(data)+".html"
            if qrcode.objects.filter(name=data).exists()==False:
                cont=qrcode()
                cont.name=data
                cont.location=loc
                cont.extinct=ext
                img = make(dat)
                img_name = 'qr' + str(data) + '.png'
                img.save(str(settings.MEDIA_ROOT)+ '/' + str(img_name))
                hello=str(settings.MEDIA_ROOT)+ '/' + str(img_name)
                cont.img=hello
                cont.save()
                messages.success(request, 'qr generated successfully , the qr is not changed if the same name is enetered again')
                return render(request, 'register.html')
            else:
                messages.warning(request, 'Name already exists , qr not changed')
        return render(request, 'register.html')
    else:
        return redirect('login')
def qrdis(request):
    if log==True:
        if request.method=='POST':
            data1=request.POST['name']
            if qrcode.objects.filter(name=data1).exists()==False:
                messages.warning(request, 'Name does not exists')
            else:
                image=qrcode.objects.filter(name=data1).all()
                return render(request, 'search.html', {'img': image})
        return render(request, 'search.html')
    else:
        return redirect('login')
def adduser(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        passw =request.POST['pass']
        cpass =request.POST['cpass']
        if Signup.objects.filter(name=name).exists():
            messages.warning(request, 'User already exists')
        if Signup.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exists')
        if passw!=cpass:
            messages.warning(request, 'Passwords do not match')
        else:
            signup=Signup(name=name, email=email, password=passw, confpassword=cpass)
            signup.save()
            messages.success(request, 'You have signed up successfully , now login')
        return redirect('signup')
def signup(request):
    if log==False:
        return render(request , 'D:/WEBSITES/DC-Django/dcanimal/templates/signup.html')
    else:
        return redirect('/')
def login(request):
    if log==False:
        return render(request , 'D:/WEBSITES/DC-Django/dcanimal/templates/login.html')
    else:
        return redirect('/')
def checklogin(request):
    if request.method=="POST":
        checklogin.email=request.POST['email']
        checklogin.passw =request.POST['pass']
        
        if Signup.objects.filter(email=checklogin.email).exists()==False and Signup.objects.filter(name=checklogin.email).exists()==False:
            messages.warning(request, 'Username does not exist , please signup')
            return redirect('login')
        if Signup.objects.filter(email=checklogin.email) or Signup.objects.filter(name=checklogin.email) and Signup.objects.filter(password=checklogin.passw):
            global log
            log=True
            return redirect('/')
        else:
            messages.error(request, 'Wrong Password')
            return redirect('login')
def home(request):
    if log==True:
        return render(request,'home.html')
    else:
        return render(request,'login.html')
def contact(request):
    if log==True:
        return render(request,'contactus.html')
    else:
        return render(request,'login.html')
def graph(request):
    if log==True:
        yes=int(qrcode.objects.filter(extinct="Yes").count())
        no=int(qrcode.objects.filter(extinct="No").count())
        africa=int(qrcode.objects.filter(location="Africa").count())
        aisa=int(qrcode.objects.filter(location="Asia").count())
        aus=int(qrcode.objects.filter(location="Australia").count())
        ant=int(qrcode.objects.filter(location="Antarctica").count())
        amazon=int(qrcode.objects.filter(location="Amazon Jungle").count())
        america=int(qrcode.objects.filter(location="America").count())
        loca=["Amazon Jungle","Africa","Asia","Australia","Antarctica","America"]
        loca_c=[amazon,africa,aisa,aus,ant,america]
        yesno=["Yes","No"]
        yesno_c=[yes,no]
        context={"yesno":yesno,"yesno_c":yesno_c,"loc":loca,"loca_c":loca_c}
        return render(request,'graph.html',context)
    else:
        return render(request,'login.html')