from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.db import connection

def keyboard(request):
    return JsonResponse({
        'type' : 'text',
    })

@csrf_exempt
def message(request):
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content']
    if return_str.isdigit() :
        cursor = connection.cursor()
        cursor.execute('select NAME from Teams where wswin = "Y" and yearid = ' + return_str)
        team = cursor.fetchall()[0][0]
        return JsonResponse({
            'message' : {
                'text' : return_str + '시즌의 우승팀은 ' + team + '입니다.'
            }
        })
    if '시즌' in return_str :
        return JsonResponse({
            'message' : {
                'text' : '검색하실 시즌을 입력하세요(1994-2016 형태로 입력)'
                }
            })
    else :
        return JsonResponse({
            'message' : {
                'text' : '임시 텍스트'
                }
            })
