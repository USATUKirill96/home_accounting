from .models import DbUser, Spending
from .serializer import Spending_Serializer


def notice_user(request=0, user_id=-1, source=-1):
    """Определяет пользоателя по входным данным (айди и источник), возвращает None, если пользователя нет"""
    if request != 0:
        pk = request.GET.get('id')
        source = request.GET.get('source')
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
    def get_spends(user):
        """Возвращает все траты пользователя"""
        spends = user.spends.all()
        return spends


class Db_Post:
    def create_database_user(site_id: int, token: str):
        user = DbUser(site_id=site_id, token=token)
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
    pass


class Db_Delete:
    pass
