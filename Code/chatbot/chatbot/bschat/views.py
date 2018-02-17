from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def keyboard(request):
    return JsonResponse({
        'type' : 'text',
    })

@csrf_exempt
def message(request):
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content']
    if return_str[-2:].isdigit() :
        request.session['season'] = int(return_str[-2:])
    if '시즌' in return_str :
        return JsonResponse({
            'message' : {
                'text' : '검색하실 시즌을 입력하세요(94-16 혹은 1994-2016 형태로 입력)'
                }
            })
    else :
        return JsonResponse({
            'message' : {
                'text' : '임시 텍스트'
                }
            })
