from .models import DbUser


def notice_user(request=None, user_id=None, source=None):
    """Notices user and returns its object using request of (user_id, source) pair.
     Returns None if user doesn't exist"""
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
    """extracts data from request. Returns positional arguments dictionary, consists of objects: user, month, year"""

    def param_parse_get(request):
        user = notice_user(request)
        month = request.GET.get('month')
        year = request.GET.get('year')
        spending_id = request.GET.get('spending_id')
        operation_id = request.GET.get('operation_id')
        category = request.GET.get('category')
        return {'user': user, 'month': month, 'year': year, 'spending_id': spending_id, 'operation_id': operation_id,
                'category': category}

    def param_parse_post(request):
        """extracts data from request. Returns positional arguments dictionary, consists of objects:
        site_id, user_id, category, name, sum, date, common, source, user, token"""
        data = request.data
        # user variables
        site_id = data.get('site_id')
        user_id = data.get('user_id')
        token = data.get('token')
        source = data.get('source')
        user = notice_user(user_id=user_id, source=source)

        # spending variables
        spending_id = data.get('spending_id')
        operation_id = data.get('operation_id')
        category = data.get('category')
        name = data.get('name')
        sum = data.get('sum')
        date = data.get('date')
        common = data.get('common')
        if common == 'True':
            common = True
        else:
            common = False

        return {'data': data, 'site_id': site_id, 'user_id': user_id, 'source': source, 'category': category,
                'name': name, 'sum': sum, 'common': common, 'user': user, 'token': token, 'date': date,
                'spending_id': spending_id, 'operation_id': operation_id}
