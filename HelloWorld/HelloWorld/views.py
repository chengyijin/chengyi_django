from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse


# def runoob(request):
#     views_list = ["诗梦", "崽崽"]
#     views_dict = {"name": "诗梦", "age": "18"}
#     views_default = []
#     now = datetime.now()
#     views_str = "<a href='https://www.runoob.com/'>点击跳转</a>"
#     views_num = 88
#     return render(request, 'runoob.html', {"views_list": views_list, "views_dict": views_dict,
#                                            "views_default": views_default, "time": now,
#                                            "views_str": views_str, "views_num": views_num})


def runoob(request):
    # name = request.GET.get("name")
    # name = request.POST.get("name")
    # name = request.body
    # name = request.path
    # name = request.method
    return HttpResponse("<a href='https://www.runoob.com/'>菜鸟教程</a>")
