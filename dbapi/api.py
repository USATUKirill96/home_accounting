from .models import DbUser


def notice_user(request=None, user_id=None, source=None):
    """Определяет пользоателя по входным данным (айди и источник), возвращает None, если пользователя нет"""
    if request is not None:
        source, user_id = request.GET.get('source'), request.GET.get('user_id')
    else:
        user_id = user_id
        source = source
    try:
        if source == "telegram":
            user = DbUser.objects.get(tg_id=user_id)
        elif source == "vk":
            user = DbUser.objects.get(vk_id=user_id)
        elif source == "site":
            user = DbUser.objects.get(site_id=user_id)
        else:
            user = None
        return user
    except Exception:
        return None


class Parser:
    def param_parse_get(request):
        user = notice_user(request)
        month = request.GET.get('month')
        year = request.GET.get('year')
        return {'user': user, 'month': month, 'year': year}

    def param_parse_post(request):
        data = request.data
        site_id = data.get('site_id')
        user_id = data.get('user_id')
        category = data.get('category')
        name = data.get('name')
        sum = data.get('sum')
        date = data.get('date')
        common = data.get('common')
        if common == 'True':
            common = True
        else:
            common = False
        source = data.get('source')
        user = notice_user(user_id=user_id, source=source)
        token = data.get('token')
        return {'data': data, 'site_id': site_id, 'user_id': user_id, 'source': source, 'category': category,
                'name': name, 'sum': sum, 'common': common, 'user': user, 'token': token, 'date':date}
