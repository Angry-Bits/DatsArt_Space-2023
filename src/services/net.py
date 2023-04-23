import json
from typing import Any

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


# Управление уровнями
URL_NEXT_LEVEL_INFO = 'http://api.datsart.dats.team/art/stage/next'
URL_NEXT_LEVEL_START = 'http://api.datsart.dats.team/art/stage/next-start'
URL_CURRENT_LEVEL_INFO = 'http://api.datsart.dats.team/art/stage/info'
URL_FINISH_LEVEL = 'http://api.datsart.dats.team/art/stage/finish'
# Фабрика красок
URL_PAINTS_GENERATION = 'http://api.datsart.dats.team/art/factory/generate'
URL_CHANGE_PAINT = 'http://api.datsart.dats.team/art/factory/pick'
# Склад краски
URL_COLORS_INFO = 'http://api.datsart.dats.team/art/colors/info'
URL_COLORS_AMOUNT = 'http://api.datsart.dats.team/art/colors/amount'
URL_GET_COLORS_LIST = 'http://api.datsart.dats.team/art/colors/list'
# Катапульта
URL_SHOT_PARAMETERS = 'http://api.datsart.dats.team/art/ballista/shoot'
# Тактовый генератор
URL_TICK_GENERATION = 'http://api.datsart.dats.team/art/state/tick'
# Очередь
URL_STATE_QUEUE = 'http://api.datsart.dats.team/art/state/queue'

TEAM_TOKEN = '642ffd078bee3642ffd078bee5'
BOUNDARY = '----WebKitFormBoundary7MA4YWxkTrZu0gW'


# Управление уровнями

def get_info_about_next_level(url: str = URL_NEXT_LEVEL_INFO) -> Any:
    '''Информация о следующем уровне.'''
    headers = {'Authorization': f'Bearer {TEAM_TOKEN}',
               'Content-Type': f'multipart/form-data; boundary={BOUNDARY}'}
    r = requests.post(url, headers=headers)
    data = json.loads(r.text)
    return data


def start_next_level(selected_image_id: int, url: str = URL_NEXT_LEVEL_START) -> Any:
    '''Старт следующего уровня.'''
    warning_answer = input('ВНИМАНИЕ! Опасный запрос! ' +
        'Вернуться и выбрать другую картинку будет нельзя. \n' +
        'Вы уверены, что хотите продолжить (да/нет)?')
    if warning_answer.lower() == 'да':
        headers = {
            "Authorization": f"Bearer {TEAM_TOKEN}",
            "Content-Type": "multipart/form-data",
        }
        multipart_data = MultipartEncoder(
            fields={
                "imageId": str(selected_image_id),
            }
        )
        headers["Content-Type"] = multipart_data.content_type

        r = requests.post(url, headers=headers, data=multipart_data)
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


def finish_current_level(url: str = URL_CURRENT_LEVEL_INFO) -> Any: # ToDo: проверить
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


# Фабрика красок

def generate_paints(url: str = URL_PAINTS_GENERATION) -> Any:
    '''Генерация краски.'''
    headers = {'Authorization': f'Bearer {TEAM_TOKEN}',
               'Content-Type': f'multipart/form-data; boundary={BOUNDARY}'}
    r = requests.post(url, headers=headers)
    data = json.loads(r.text)
    return data


def change_paint(selected_paint_id: int, url: str = URL_CHANGE_PAINT) -> Any:
    '''Выбор краски.'''
    headers = {
        "Authorization": f"Bearer {TEAM_TOKEN}",
        "Content-Type": "multipart/form-data",
    }
    multipart_data = MultipartEncoder(
        fields={
            "num": str(selected_paint_id)
        }
    )
    headers["Content-Type"] = multipart_data.content_type

    r = requests.post(url, headers=headers, data=multipart_data)
    data = json.loads(r.text)
    return data


# Склад краски

def colors_info(url: str = URL_COLORS_INFO) -> Any:
    '''Общая информация об имеющемся количестве уникальных цветов
    и общем количестве краски.'''
    headers = {
        "Authorization": f"Bearer {TEAM_TOKEN}",
        "Content-Type": "multipart/form-data",
    }
    r = requests.post(url, headers=headers)
    data = json.loads(r.text)
    return data


def colors_amount(selected_color: int, url: str = URL_COLORS_AMOUNT) -> Any:
    '''Запрос остатков краски.'''
    headers = {
        "Authorization": f"Bearer {TEAM_TOKEN}",
        "Content-Type": "multipart/form-data",
    }
    multipart_data = MultipartEncoder(
        fields={
            "color": str(selected_color)
        }
    )
    headers["Content-Type"] = multipart_data.content_type

    r = requests.post(url, headers=headers, data=multipart_data)
    data = json.loads(r.text)
    return data


def get_color_list(url: str = URL_GET_COLORS_LIST) -> Any:
    '''Список всех остатков.'''
    headers = {
        "Authorization": f"Bearer {TEAM_TOKEN}",
        "Content-Type": "multipart/form-data",
    }
    r = requests.post(url, headers=headers)
    data = json.loads(r.text)
    return data


# Катапульта

def adjust_shot_parameters(angle_horizontal: int,
                           angle_vertical: int,
                           power: int,
                           colors: list,
                           url: str = URL_SHOT_PARAMETERS): # ToDo: проверить
    '''Параметры выстрела.'''
    headers = {
        "Authorization": f"Bearer {TEAM_TOKEN}",
        "Content-Type": "multipart/form-data",
    }
    fields = {
        "angleHorizontal": str(angle_horizontal),
        "angleVertical": str(angle_vertical),
        "power": str(power),
    }
    for color, amount in colors.items():
        fields[f"colors[{color}]"] = str(amount)

    multipart_data = MultipartEncoder(fields=fields)
    headers["Content-Type"] = multipart_data.content_type

    r = requests.post(url, headers=headers, data=multipart_data)
    data = json.loads(r.text)

    return data


# Тактовый генератор

def generate_tick(url: str = URL_TICK_GENERATION) -> Any:
    '''Генерация тактового генератора.'''
    headers = {'Authorization': f'Bearer {TEAM_TOKEN}',
               'Content-Type': f'multipart/form-data; boundary={BOUNDARY}'}
    r = requests.post(url, headers=headers)
    data = json.loads(r.text)
    return data


# Очередь

def check_queue_status(name: str, url: str = URL_STATE_QUEUE) -> Any:
    '''Узнать состояние очереди.'''
    headers = {
        "Authorization": f"Bearer {TEAM_TOKEN}",
        "Content-Type": "multipart/form-data",
    }
    multipart_data = MultipartEncoder(
        fields={
            "name": name
        }
    )
    headers["Content-Type"] = multipart_data.content_type

    r = requests.post(url, headers=headers, data=multipart_data)
    data = json.loads(r.text)
    return data


if __name__ == '__main__':
    #print(generate_paints())
    #print(change_paint(1))
    print(get_info_about_current_level())
