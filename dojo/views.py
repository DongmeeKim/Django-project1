from django.shortcuts import render
from django.http import HttpResponse

def mysum(request, numbers):
    result = sum(map(lambda s: int(s or 0), numbers.split("/"))) # 다수의 /로 이루어진 주소의 문자열을 모두 더하는 경우
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요.'.format(name,age))


def post_list1(request):
    name = '공유'
    return HttpResponse('''
<h1> ASK Django </h1>

<p> {name} </p>

<p> 여러분의 파이썬 & 장고 페이스메이커가 되겠습니다. </p>   '''.format(name=name))


def post_list2(request):
    name = '공유'
    response = render(request, 'dojo/post_list.html', {'name': name})
    return response

