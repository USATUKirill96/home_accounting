from .models import DbUser, Spending


def notice_user(pk: int, source: str):
    """Определяет пользоателя по входным данным (айди и источник), возвращает None, если пользователя нет"""
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
    def create_database_user(site_id:int, token:str):
        user = DbUser(site_id=site_id, token=token)
        user.save()
        return user

    def create_spending(user, **kwargs):
        spending = Spending.objects.create(user=user, **kwargs)
        spending.save()
        return spending




class Db_Put:
    pass


class Db_Delete:
    pass


print(notice_user(1, 'telegram'))
