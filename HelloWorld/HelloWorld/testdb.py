from django.http import HttpResponse

from TestModel.models import Test


def save(request):
    test1 = Test(name='诗诗')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")


def search(request):
    response1 = ""
    response2 = ""
    response3 = ""
    list1 = Test.objects.all()
    list2 = Test.objects.filter(id=1)
    list3 = Test.objects.get(id=1)
    for list in list1:
        response1 += list.name
    for list in list2:
        response2 += list.name
    response3 += list3.name
    return HttpResponse(response1+"+++"+response2+"+++"+response3)


def update(request):
    # test1 = Test.objects.get(id=1)
    # test1.name = 'Google'
    # test1.save()
    Test.objects.filter(id=1).update(name='Google')
    # 修改所有的列
    # Test.objects.all().update(name='Google')

    return HttpResponse("<p>修改成功</p>")


def delete(request):
    # 删除id=1的数据
    # test1 = Test.objects.get(id=1)
    # test1.delete()

    # 另外一种方式
    Test.objects.filter(id=1).delete()

    # 删除所有数据
    # Test.objects.all().delete()

    return HttpResponse("<p>删除成功</p>")


