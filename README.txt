Формат запроса для получения данных о покупках:
a = requests.get('http://localhost:8000/api/spends?user_id=4&source=vk')
Где id - идентификатор пользователя в сервисе, source - код сервиса (vk, telegram, site)

Формат запроса для внесения покупки в базу:
requests.post('http://localhost/api/spends/', data = {'user_id':'1', 'source':'vk', 'category': 'продукты',
                                                        'name':'Кулич', 'sum':100, 'common':'False'})

Привязка мессенджера пользователя по токену:
data = requests.put('http://127.0.0.1:8000/api/users/', data = {'user_id':'1', 'source':'vk', 'token':"token1"})

Регистрация пользователя
data = requests.post('http://127.0.0.1:8000/api/users/', data = {'site_id':'2'})

Валидация пользователя по идентефикатору источника и наименованию источника
result = requests.get('http://localhost:8000/api/validate?user_id=4&source=vk')

