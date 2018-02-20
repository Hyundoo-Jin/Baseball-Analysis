from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
from bschat.models import Teams
from urllib.request import urlopen
from django.db import connection


def keyboard(request):
    return JsonResponse({
        'type': 'text'
    })


@csrf_exempt
def message(request):
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content']
    if(return_str.find(u"야구")>-1):
        return JsonResponse({
        'message' : {
            'text' : '지구별 우승인지 월드시리지 우승인지를 적어주세요!'
        },
        'keyboard': {
            'type': 'text'
        }
        })
    elif(return_str.find("우승")>-1 and + return_str.find("월드시리즈")>-1 and return_str[:4].isdigit()):
        cursor = connection.cursor()
        cursor.execute('select NAME, attendance from Teams where wswin = "Y" and yearid = ' + return_str[:4])
        team, attend = cursor.fetchall()[0]
        return JsonResponse({
            'message' : {
                'text' : 'MLB ' + return_str[:4] + '시즌의 월드시리즈 우승팀은 ' + team + '입니다.\n총 누적 관중수는 ' + str(attend) + ' 명 입니다'
            }
        })
    elif (return_str.find("순위") > -1 and return_str[:4].isdigit()):
        cursor = connection.cursor()
        cursor.execute('select NAME, rank from Teams where yearid = ' + return_str[:4] + ' order by rank ASC')
        result = ''
        for team, rank in cursor.fetchall():
            result += team + '\n팀 순위는 ' + str(rank) + '위 입니다. \n'
        return JsonResponse({
            'message': {
                'text': result
            }
        })

    elif (return_str.find("지구") > -1 and return_str.find("우승") > -1 and return_str[:4].isdigit()):
        cursor = connection.cursor()
        cursor.execute(
            'select NAME, divID, lgID from Teams where Divwin = "Y" and yearid = ' + return_str[:4] + ' order by divID')
        result = ''
        for team, div, lg in cursor.fetchall():
            result += div + ' 지구 ' + lg + '리그 우승팀은\n ' + str(team) + ' 입니다. \n'
        return JsonResponse({
            'message': {
                'text': result
            }
        })
    elif(return_str.find("최고")>-1 or return_str.find("mvp")>-1 and return_str[:4].isdigit()):
        cursor = connection.cursor()
        cursor.execute('select playerID from AwardsPlayers where awardID = "World Series MVP" and yearID = ' + return_str[:4])
        player = cursor.fetchall()[0][0]
        return JsonResponse({
            'message' : {
                'text' : return_str[:4] + '시즌 월드시리즈 MVP는 ' + player[0:-2] + ' 입니다'
            }
        })

    elif(return_str.find("안녕")>-1 or return_str.find("하이")>-1):
        return JsonResponse({
        'message' : {
            'text' : '네 안녕하세요^^'
        },
        'keyboard': {
            'type': 'text'
        }
        })

    elif (return_str.find("배고파") > -1 or return_str.find("밥줘") > -1 or return_str.find("배고프다") > -1):
        return JsonResponse({
            'message': {
                'text': '저런ㅠㅠ 어서 사드세요'
            },
            'keyboard': {
                'type': 'text'
            }
        })
    elif (return_str.find("심심") > -1 or return_str.find("놀아줘") > -1):
        return JsonResponse({
            'message': {
                'text': '머하고 놀까요? ㅎㅎ'
            },
            'keyboard': {
                'type': 'text'
            }
        })
    else:
        return JsonResponse({
            'message': {
                'text': '무슨 말인지 잘 모르겠어요. MLB 관련 질문을 해주세요!'
            },
            'keyboard': {
                'type': 'text'
            }
        })


#def testpage(request) :
#    cursor = connection.cursor()
#    cursor.execute('select NAME, rank from Teams where yearid = ' + '2016' + ' order by rank ASC')
#    result = ''
#    for team, rank in cursor.fetchall():
#        result += team + '팀의 순위는 ' + str(rank) + '위 입니다. \n'
#    return HttpResponse(result)
