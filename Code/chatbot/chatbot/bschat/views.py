from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.db import connection

def keyboard(request):
    return JsonResponse({
        'message': {
            'text': "원하는 기능을 선택해주세요."
        },
        'type': 'buttons',
        'buttons': ['팀 검색', '시즌 검색']
    })


@csrf_exempt
def message(request):
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content']

    requestmode = return_str.encode('utf-8')
    if requestmode == '팀 검색' :
        return JsonResponse({
            'message': {
                'text': "검색을 원하는 팀의 리그를 선택해주세요."
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['American League', 'National League']
                }
            })
    elif requestmode == '시즌 검색' :
        return JsonResponse({
            'message': {
                'text': "검색을 원하는 시즌을 입력해주세요."
                        "ex) 13 -> 2013시즌, 10 -> 2010시즌"
            },
            'keyboard': {
                'type': 'text'
            }
        })