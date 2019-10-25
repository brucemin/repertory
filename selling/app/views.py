from django.shortcuts import render,redirect,HttpResponse
from app.models import *
from django.http import JsonResponse
import datetime
# Create your views here.

def login(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        user_obj = User.objects.filter(user=user, pwd=pwd).first()
        if user_obj:
            request.session["user"] = user_obj.id
            request.session["name"] = user_obj.user
            return redirect("/list_1og/")

    return render(request,"login.html")

def list_1og(request):
    list = commodity.objects.all()
    return render(request,"list.html",{"list":list})

def auction_log(request,id):
    list = commodity.objects.filter(id=id)
    name=request.session.get("name")
    a_id = request.session.get("user")
    a  = commodity.objects.get(id=id)
    text =  ""
    try:
        if request.method == "POST":
            a_price = request.POST.get("price")
            if float(a_price) < a.prict:
                text = "不能低于起始价格"
            else:
                res = auction.objects.filter(a_price__gt=float(a_price)).values("a_price")
                if res :
                    text = "不能低于最高竞拍价"
                else:
                    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    auction.objects.create(c_id_id=id,a_price=a_price,stop=now,u_id_id=a_id,u_name=name)
    except Exception as e:
        print(e)
    auction_obj = auction.objects.filter(c_id_id=id).all().order_by("-a_price")
    return render(request,"auction.html",{"list":list,"auction_obj":auction_obj,"text":text})

def result(request):
    c_id = commodity.objects.all()
    name=request.session.get("name")
    list = []
    for i in c_id:
        print(i.id)
        auction_obj = auction.objects.filter(c_id=i.id).order_by("a_price")
        print(auction_obj)
        for j in auction_obj:
            a_price = j.a_price
            a_name = j.u_name
        if auction_obj:
            list.append({"name":i.name,"start":i.start,"stop":i.start,"price":i.prict,"a_price":a_price,"a_name":a_name})
        else:
            pass
    return render(request,"result.html",{"key":list,"name":name})

def reg(request):
    text = ""
    if request.method == "POST":
        user = request.POST.get("user")
        pwd_1 = request.POST.get("pwd_1")
        pwd_2 = request.POST.get("pwd_2")
        user_obj = User.objects.filter(user=user).first()

        if user_obj:
            text = "用户名已存在"
        else:
            if pwd_1 == pwd_2:
                User.objects.create(user=user,pwd=pwd_2)
                return redirect("/login/")
            else:
                text = "两次密码不一样"
    return render(request,"reg.html",{"text":text})


def add(request):
    commodity.objects.create(name = '虎符',start = '2019-09-11',stop='2019-10-11',prict='50000',describe='调兵')
    return HttpResponse('添加完成')