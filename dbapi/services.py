from .models import DbUser, Spending
from .serializer import Spending_Serializer


def notice_user(request=None, user_id=None, source=None):
    """Определяет пользоателя по входным данным (айди и источник), возвращает None, если пользователя нет"""
    if request is not None:
        source, pk = request.GET.get('source'), request.GET.get('id')
    else:
        pk = user_id
        source = source
    try:
        if source == "telegram":
            user = DbUser.objects.get(tg_id=pk)
        elif source == "vk":
            user = DbUser.objects.get(vk_id=pk)
        elif source == "site":
            user = DbUser.objects.get(site_id=pk)
        else:
            user = None
        return user
    except Exception:
        return None


class Db_Get:
    def get_spends(request):
        """Возвращает все траты пользователя"""
        user = notice_user(request=request)
        spends = user.spends.all()
        return spends


class Db_Post:
    def create_database_user(request):
        site_id = request.data.get('user_id')
        token = request.data.get('token')
        user = DbUser.objects.create(site_id=site_id, token=token)
        user.save()
        return user

    def create_spending(request):
        data = request.data
        user_id = data.get('user_id')
        service = data.get('source')
        category = data.get('category')
        name = data.get('name')
        sum = data.get('sum')
        common = data.get('common')

        user = notice_user(user_id=user_id, source=service)
        if common == 'True':
            common = True
        else:
            common = False
        obj = Spending.objects.create(user=user, category=category, name=name, sum=sum, common=common)
        return obj.name, obj.sum


class Db_Put:
    def add_messenger(request):
        source, id = request.data.get('source'), request.data.get('user_id')
        token = request.data.get('token')
        print(token)
        user = DbUser.objects.get(token=token)
        if source == 'vk':
            user.vk_id = id
        else:
            user.tg_id = id
        user.save()
        return user


class Db_Delete:
    pass
