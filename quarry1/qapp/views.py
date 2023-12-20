from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import UserRegistration,Admin,Item,Cart
# Create your views here.
def user_register(request):
    if request.method=='POST':
        uname=request.POST['name']
        uaddress = request.POST['address']
        uplace = request.POST['place']
        uemail = request.POST['email']
        uphone = request.POST['phone']
        uuser = request.POST['username']
        upass = request.POST['password']
        data=UserRegistration.objects.create(u_name=uname,u_address=uaddress,u_place=uplace,u_email=uemail,u_contact=uphone,username=uuser,password=upass)
        data.save()
        return HttpResponse("Yes, User Registered")
    else:
        return render(request,'index.html')


def admin_register(request):
        uname="admin"
        upassw = "admin"
        Admin.objects.create(admin_id=uname,password=upassw)
        return HttpResponse("yes")

# def showlog(request):
#     return render(request,'login.html')
def log(request):
    if request.method=='POST':
        uuser=request.POST['user']
        passw=request.POST['pass']
        try:
            data=UserRegistration.objects.filter(username=uuser,password=passw)
            print(uuser)
            print(passw)
            print(data)
            if data.exists():
                print("ok user")
                request.session['user_in']=uuser
                return render(request,'userdash.html')
            else:
                # return render(request,'login.html')
                data = Admin.objects.filter(admin_id=uuser,password=passw)
                print(passw)
                print(data)
                if data.exists():
                    print("ok admin")
                    request.session['admin_in'] = passw
                    return render(request, 'admindash.html')
                else:
                    return render(request, 'index.html')
        except Exception:
            print("error")
            return HttpResponse("Incorrect Username")
    else:
        return render(request,'index.html')

def ind(request):
    return render(request,'index.html')
def indh(request):
    return render(request,'indexhead.html')

def addproduct(request):
    if request.method=="POST":
        iname=request.POST['pname']
        iquan = request.POST['pquant']
        iprice = request.POST['prate']
        iimage = request.POST['pimg']
        data=Item.objects.create(item_name=iname,item_quantity=iquan,item_price=iprice,item_img=iimage)
        data.save()
        return HttpResponse("Product Added")
    else:
        return render(request,'addproduct.html')

def uploadProduct(request):
    if request.method == "POST":
        iname = request.POST['pname']
        iquan = request.POST['pquant']
        iprice = request.POST['prate']
        iimage = request.POST['pimg']
        data = Item.objects.create(item_name=iname, item_quantity=iquan, item_price=iprice, item_img=iimage)
        return HttpResponse("<script>alert('product added');</script>")
        # window.location = 'vprod';
    else:
        return render(request, 'addproduct.html')

def adlogout(request):
    if 'admin_in' in request.session:
        request.session.flush()
        return redirect(ind)
    else:
        return redirect(ind)


