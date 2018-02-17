from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.db import connection

def keyboard(request):
    return JsonResponse({
        'message': {
            'text' : '안녕하세요? 시즌별 메이저리그 팀 성적을 알려드리는 챗봇입니다.'
        }
    })


@csrf_exempt
def message(request):
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content']

    requestmode = return_str.encode('utf-8')
    if '시즌' in requestmode :
        season = int(requestmode[requestmode.find('시즌') - 1 : requestmode.find('시즌')])
    return JsonResponse({
        'message' : {
            'text' : season
        }
    })