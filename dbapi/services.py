import secrets

from .models import DbUser, Spending


def token_generator():
    """Generates unique token. If there is same token in database, tries another variant"""
    token_found = False
    while not token_found:
        token = secrets.token_hex(32)
        try:
            DbUser.objects.get(token=token)
        except:
            token_found = True
        return token


class Db_Get:
    def get_spends(**kwargs):
        """Returns user's spendings for a period of month. It takes three named arguments: user, month and year.
        Returns a tuple of spends objects, sorted byy -date"""
        if not kwargs['month']:
            spends = kwargs['user'].spends.filter(date__year=kwargs['year']).order_by('-date')
        else:
            spends = kwargs['user'].spends.filter(date__year=kwargs['year']).filter(
                date__month=kwargs['month']).order_by('-date')
        return spends

    def validate_user(**kwargs):
        """validates if user exist, using parser data. Returns True or False in response"""
        print(kwargs['user'])
        if kwargs['user'] is not None:
            return True
        else:
            return False


class Db_Post:
    def create_database_user(**kwargs):
        """Registers user in database. Takes user_id from site and generates token to add messengers.
        Returns token"""
        token = token_generator()
        user = DbUser.objects.create(site_id=kwargs['user_id'], token=token)
        user.save()
        return user.token

    def create_spending(**kwargs):
        """Registers spending in database. Takes user object and spending attributes:
         category, name, sum, date, common. Returns name and sum of spending."""
        obj = Spending.objects.create(user=kwargs['user'], category=kwargs['category'],
                                      name=kwargs['name'], sum=kwargs['sum'], common=kwargs['common'],
                                      date=kwargs['date'])
        return obj.name, obj.sum


class Db_Put:
    def edit_messenger(**kwargs):
        """Registers messenger in database. Takes three named arguments: source (vk, telegram), user_id,
        token"""
        user = DbUser.objects.get(token=kwargs['token'])
        if kwargs['source'] == 'vk':
            user.vk_id = kwargs['user_id']
        else:
            user.tg_id = kwargs['user_id']
        user.save()
        return user

    def edit_spending(**kwargs):
        """Changes spending object in database. Takes named arguments:
        spending_id, category, name, sum, common, date. Returns redacted object."""
        redacted_spending = Spending.objects.get(id=kwargs['spending_id'])
        redacted_spending.category = kwargs['category'] or redacted_spending.category
        redacted_spending.name = kwargs['name'] or redacted_spending.name
        redacted_spending.sum = kwargs['sum'] or redacted_spending.sum
        redacted_spending.common = kwargs['common'] or redacted_spending.common
        redacted_spending.date = kwargs['date'] or redacted_spending.date
        redacted_spending.save()
        return redacted_spending


class Db_Delete:
    def delete_spending(**kwargs):
        """Deletes chosen spending. Takes spending_id, returns number of deleted objects if deleting is successful"""
        object_to_delete = Spending.objects.get(id=kwargs['spending_id'])
        objects_deleted = object_to_delete.delete()
        return objects_deleted
