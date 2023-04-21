import json
from typing import Any

import requests


URL_NEXT_LEVEL_INFO = 'http://api.datsart.dats.team/art/stage/next'
URL_NEXT_LEVEL_START = 'http://api.datsart.dats.team/art/stage/next-start'
URL_CURRENT_LEVEL_INFO = 'http://api.datsart.dats.team/art/stage/info'
URL_FINISH_LEVEL = 'http://api.datsart.dats.team/art/stage/finish'
TEAM_TOKEN = '642ffd078bee3642ffd078bee5'
BOUNDARY = '----WebKitFormBoundary7MA4YWxkTrZu0gW'


def get_info_about_next_level(url: str = URL_NEXT_LEVEL_INFO) -> Any:
    '''Информация о следующем уровне.'''
    headers = {'Authorization': f'Bearer {TEAM_TOKEN}',
               'Content-Type': f'multipart/form-data; boundary={BOUNDARY}'}
    r = requests.post(url, headers=headers)
    data = json.loads(r.text)
    return data


def start_next_level(image_id: int, url: str = URL_NEXT_LEVEL_START) -> Any:
    '''Старт следующего уровня.'''
    warning_answer = input('ВНИМАНИЕ! Опасный запрос! ' +
        'Вернуться и выбрать другую картинку будет нельзя. \n' +
        'Вы уверены, что хотите продолжить (да/нет)?')
    if warning_answer.lower() == 'да':
        headers = {'Authorization': f'Bearer {TEAM_TOKEN}',
                   'Content-Type': f'multipart/form-data; boundary={BOUNDARY}',
                   'Content-Disposition': f"form-data; name='{image_id}'"}
        r = requests.post(url, headers=headers)
        data = json.loads(r.text)
        return data
    else:
        return 'Выход...'


def get_info_about_current_level(url: str = URL_CURRENT_LEVEL_INFO) -> Any:
    '''Информация о текущем уровне.'''
    headers = {'Authorization': f'Bearer {TEAM_TOKEN}',
               'Content-Type': f'multipart/form-data; boundary={BOUNDARY}'}
    r = requests.post(url, headers=headers)
    data = json.loads(r.text)
    return data


def finish_current_level(url: str = URL_CURRENT_LEVEL_INFO) -> Any:
    '''Завершить уровень.'''
    warning_answer = input('ВНИМАНИЕ! Опасный запрос! ' +
        'Вернуться и исправить уровень. \n' +
        'Вы уверены, что хотите продолжить (да/нет)?')
    if warning_answer.lower() == 'да':
        headers = {'Authorization': f'Bearer {TEAM_TOKEN}',
                'Content-Type': f'multipart/form-data; boundary={BOUNDARY}'}
        r = requests.post(url, headers=headers)
        data = json.loads(r.text)
        return data
    else:
        return 'Выход...'
