from django.shortcuts import render
from .models import School
import csv
import json
import urllib.request

# Create your views here.

def index(request):

  client_id = "DshukL7WQcANLYUiQTsY" # 네이버에서 받은 클라이언트 아이디 
  client_secret = "p5RxLlzjyJ" # secret 넘버

  encText = urllib.parse.quote("{}".format('복지')) 
  url = "https://openapi.naver.com/v1/search/news?query=" + encText # url 입력하기 
  movie_api_request = urllib.request.Request(url)
  movie_api_request.add_header("X-Naver-Client-Id", client_id)
  movie_api_request.add_header("X-Naver-Client-Secret", client_secret)
  response = urllib.request.urlopen(movie_api_request) 
  rescode = response.getcode()
  if (rescode == 200):
    response_body = response.read()
    result = json.loads(response_body.decode('utf-8'))
    items = result.get('items') #받아온 데이터 변수에 저장

    context = {
        'items':items,
      }

    return render(request, 'hadiedu/index.html', context=context)



def search(request):
  
  if request.method == 'POST':

    q = request.POST.get('q')

    eschools = School.objects.filter(address__contains = q, sname__contains = '초등')
    mschools = School.objects.filter(address__contains = q, sname__contains = '중학')
    hschools = School.objects.filter(address__contains = q, sname__contains = '고등')


    context ={
    'eschools':eschools, 
    'mschools':mschools, 
    'hschools':hschools,  
      }

    return render(request, 'hadiedu/index.html', context)






def detail(request):
  if request.method == 'POST':
    a = request.POST.get('a')

    schools = School.objects.filter(sname__contains = a)
    client_id = "DshukL7WQcANLYUiQTsY" # 네이버에서 받은 클라이언트 아이디 
    client_secret = "p5RxLlzjyJ" # secret 넘버

    encText = urllib.parse.quote("{}".format('복지')) 
    url = "https://openapi.naver.com/v1/search/news?query=" + encText # url 입력하기 
    movie_api_request = urllib.request.Request(url)
    movie_api_request.add_header("X-Naver-Client-Id", client_id)
    movie_api_request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(movie_api_request) 
    rescode = response.getcode()
    if (rescode == 200):
      response_body = response.read()
      result = json.loads(response_body.decode('utf-8'))
      items = result.get('items') #받아온 데이터 변수에 저장

    context ={
    'schools':schools,
    'items':items, 
    
      }
    return render(request, 'hadiedu/detail.html', context)

