from django.shortcuts import render, redirect
from LoginModel import models


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("username")
    password = request.POST.get("pwd")
    user_obj = models.UserInfo.objects.filter(username=username, password=password).first()

    if not user_obj:
        return redirect("/login/")
    else:
        rep = redirect("/index/")
        rep.set_cookie("is_login", True)
        return rep


def index(request):
    status = request.COOKIES.get('is_login')  # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    if not status:
        return redirect('/login/')
    return render(request, "index.html")


def logout(request):
    rep = redirect('/login/')
    rep.delete_cookie("is_login")
    return rep  # 点击注销后执行,删除cookie,不再保存用户状态，并弹到登录页面


def order(request):
    status = request.COOKIES.get('is_login')
    if not status:
        return redirect('/login/')
    return render(request, "order.html")