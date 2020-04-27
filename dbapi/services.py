import secrets
from django.db.models import Q

from .models import DbUser, Spending, Income


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
    def get_operations(unsorted_objects, year, month):
        q = Q(date__year=year) & Q(date__month=month)
        if month:
            return unsorted_objects.filter(q).order_by('-date')
        else:
            return unsorted_objects.filter(date__year=year).order_by('-date')

    def get_spends(**kwargs):
        """Returns user's spendings for a period of month. It takes three named arguments:
         user, year and month (optional). Returns a tuple of spends objects, sorted byy -date"""
        all_spends = kwargs['user'].spends
        try:
            return Db_Get.get_operations(all_spends, kwargs['year'], kwargs['month'])
        except:
            return None

    def get_incomes(**kwargs):
        """Returns user's incomes for a chosen period (tuple). Takes 3 named arguments: user, year, month (optional)"""
        try:
            all_incomes = kwargs['user'].incomes
            return Db_Get.get_operations(all_incomes, kwargs['year'], kwargs['month'])
        except:
            return None

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

    def create_income(**kwargs):
        obj = Income.objects.create(user=kwargs['user'], name=kwargs['name'], sum=kwargs['sum'], date=kwargs['date'])
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

    def edit_operation(operation, name, sum, date, category=None):
        operation.name = name or operation.name
        operation.sum = sum or operation.sum
        operation.date = date or operation.date
        try:
            operation.category = category or operation.category
        except:
            pass
        operation.save()
        return operation

    def edit_spending(**kwargs):
        """Changes spending object in database. Takes named arguments:
        spending_id, category, name, sum, common, date. Returns redacted object."""
        try:
            redacted_spending = kwargs['user'].spends.get(id=kwargs['spending_id'])
        except:
            return False
        return Db_Put.edit_operation(redacted_spending, kwargs['name'], kwargs['sum'],
                                     kwargs['date'], kwargs['category'])

    def edit_income(**kwargs):
        """Changes income object in database. Takes named arguments:
        operation_id, name, sum, date. Returns redacted object."""
        try:
            redacted_income = kwargs['user'].incomes.get(id=kwargs['operation_id'])
        except:
            return False
        return Db_Put.edit_operation(redacted_income, kwargs['name'], kwargs['sum'], kwargs['date'])


class Db_Delete:
    def delete_spending(**kwargs):
        """Deletes chosen spending. Takes spending_id, returns number of deleted objects if deleting is successful"""
        object_to_delete = Spending.objects.get(id=kwargs['spending_id'])
        objects_deleted = object_to_delete.delete()
        return objects_deleted

    def delete_income(**kwargs):
        """Deletes chosen income. Takes operation_id, returns number of deleted objects if deleting is successful"""
        object_to_delete = Income.objects.get(id=kwargs['operation_id'])
        objects_deleted = object_to_delete.delete()
        return objects_deleted
