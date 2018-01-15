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



def input(request):

  line = []
  line1 = []

  f = open('장애인편의.csv', 'r', encoding='mac_roman' ,  newline='')
  rdr = csv.reader(f)

  for row in rdr:
    line.insert(0,row)
    for lines in line:
      school = School(
        eduoffice = lines[0],
        code = lines[3],
        sname = lines[4],
        diff= lines[6],
        Enter  = lines[9],
        parking = lines[10],
        enhi  = lines[11],
        hallway = lines[12],
        hsupport = lines[13],
        hfeces = lines[14],
        hufine = lines[15],
        braille = lines[16],
        announce = lines[17],
        alarm = lines[18],
        address = lines[1],
        daddress = lines[2],
        pnum = lines[7],
        haddress = lines[5],
        sex = lines[8],
        )
      school.save()

  return render(request, 'hadiedu/index.html')
