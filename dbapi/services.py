import secrets
from .models import DbUser, Spending
from .serializer import Spending_Serializer


class Db_Get:
    def get_spends(**kwargs):
        """Возвращает все траты пользователя"""
        spends = kwargs['user'].spends.all()
        return spends

    def validate_user(**kwargs):
        print(kwargs['user'])
        if kwargs['user'] is not None:
            return True
        else:
            return False


class Db_Post:
    def create_database_user(**kwargs):
        token = secrets.token_hex(32)
        user = DbUser.objects.create(site_id=kwargs['site_id'], token=token)
        user.save()
        return user.token

    def create_spending(**kwargs):
        obj = Spending.objects.create(user=kwargs['user'], category=kwargs['category'],
                                      name=kwargs['name'], sum=kwargs['sum'], common=kwargs['common'])
        return obj.name, obj.sum


class Db_Put:
    def add_messenger(**kwargs):
        user = DbUser.objects.get(token=kwargs['token'])
        if kwargs['source'] == 'vk':
            user.vk_id = kwargs['user_id']
        else:
            user.tg_id = kwargs['user_id']
        user.save()
        return user


class Db_Delete:
    pass
