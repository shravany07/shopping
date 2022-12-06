from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.db.models import Q


from app1.models import  Pro, Signup, contact_us, fpro

# Create your views here.
def index(request):
    if 'xyz' in request.session.keys():
        f=fpro.objects.all()
        return render(request,'index.html',{'f':f})
    else:
        return redirect('login')

def about(request):
    if 'xyz' in request.session.keys():
        return render(request,'about.html')
    else:
        return redirect('login')
    
def contact(request):
    if 'xyz' in request.session.keys():
        if request.method=='POST':
            model=contact_us()
            model.name=request.POST['name']
            model.email=request.POST['email']
            model.phone=request.POST['phone']
            model.message=request.POST['message']
            model.save()
        return render(request,'contact.html')
    else:
        return redirect('login')

def jewellery(request):
    if 'xyz' in request.session.keys():
        l=Pro.objects.all()
        return render(request,'jewellery.html',{'l':l})
    else:
        return redirect('login')

def login(request):
    if request.method=='POST':
        try:
            m=Signup.objects.get(email_id=request.POST['user'])
            if m.password==request.POST['pass']:
                request.session['xyz']=m.id
                return redirect('index')
            else:
                return HttpResponse('wrong password')
        except:
            return HttpResponse('wrong email')

    return render(request,'login.html')

def signup(request):
        if request.method=='POST':
            model=Signup()
            model.First_Name=request.POST['firstname']
            model.Last_Name=request.POST['lastname']
            model.email_id=request.POST['email']
            model.mobile_no=request.POST['mobileno']
            model.password=request.POST['pass']
            model.save()

        return render(request,'signup.html')


def productview(request,abc):
    if 'xyz' in request.session.keys():
        v=Pro.objects.get(id=abc)
        return render(request,'productview.html',{'v':v})
    else:
        return redirect('login')

def searchview(request):
    if 'xyz' in request.session.keys():
        q=request.GET.get('search')
        if q:
            pr=Pro.objects.filter(Q(name__icontains=q)| Q(des__icontains=q)| Q(price__icontains=q))
            data={'p':pr}
        else:
            data={}
        return render(request,'search.html',data)
    else:
        return redirect('login')

def logout(request):
    if 'xyz' in request.session.keys():
        del request.session['xyz']
        return redirect('login')
    else:
        return redirect ('login')

def addpro(request):
        if request.method=='POST':
            model=Pro()
            model.name=request.POST['name']
            model.des=request.POST['des']
            model.price=request.POST['price']
            model.img=request.FILES.get('image')
            model.review=request.POST['rev']
            model.save()
        return render(request,'addpro.html')