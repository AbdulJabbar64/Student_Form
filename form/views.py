from django.shortcuts import render ,redirect
from .models import Form
from django.contrib.auth.models import User, auth

# Create your views here.


class FormStd:
    def home(request):
        return render(request, 'home.html')
    
    def data(request):
        da = Form.objects.all()
        return render(request, 'data.html' ,{'da':da})
    
    def send(request):        
        na = request.POST.get('name')
        rol = request.POST.get('roll')
        dep = request.POST.get('dept')
        dat = request.POST.get('date')
        img = request.POST.get('upload')
        submit = Form(name=na,rollNa=rol, dept=dep, addmission=dat, iamge=img)
        submit.save()
        return render(request, 'home.html')

    def reg(request):
        
        if request.method == 'post':
            first = request.POST['first_name']
            last = request.POST['last_name']
            usern = request.POST['username']
            ema = request.POST['email']
            passwrod = request.POST['password1']
            passwrod1 = request.POST['password2']

            submit = User.objects.create_user(username=usern, first_name=first,last_name=last,email=ema,password=passwrod)
            submit.save()
            print('data saved')
            return redirect('/')
        else:
            print('not pass')
            return render(request, 'reg.html')