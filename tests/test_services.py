from django.test import TestCase
from dbapi.services import Db_Post, Db_Get, Db_Put, Db_Delete, notice_user
from dbapi.models import DbUser, Spending


class GetMethods(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        DbUser.objects.create(vk_id=1)
        DbUser.objects.create(vk_id=2)
        Spending.objects.create(user=DbUser.objects.get(id=1), category="продукты", name="молоко", sum=100)

    def test_notice_user(self):
        print("Method: function notice_user")
        user1 = DbUser.objects.get(id=1)
        user2 = notice_user(1, 'vk')
        self.assertEqual(user1, user2)

    def test_get_spending(self):
        print("Method: function get_spending")
        user = DbUser.objects.get(id=1)
        spending1 = user.spends.all()[0]
        spending2 = Db_Get.get_spends(user)[0]
        self.assertEqual(spending1, spending2)

    def test_user_does_not_exist(self):
        user = notice_user(-1, 'vk')
        self.assertEqual(user, None)

    def test_user_does_not_have_spends(self):
        user = DbUser.objects.get(id=2)
        spendings = user.spends
        print(spendings.name)
        self.assertEqual(spendings.name, None)


class PostMethods(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        DbUser.objects.create(vk_id=1)
        DbUser.objects.create(vk_id=2)
        Spending.objects.create(user=DbUser.objects.get(id=1), category="продукты", name="молоко", sum=100)

    def test_create_db_user(self):
        user1 = Db_Post.create_database_user(site_id=22, token='asdf')
        user2 = notice_user(22, 'site')
        self.assertEqual(user1, user2)

    def test_create_spending(self):
        user = DbUser.objects.get(id=2)
        Db_Post.create_spending(user=user, category="продукты", name="пиво", sum=32)
        spending2 = user.spends.get(sum=32)
        self.assertEqual(spending2.category, "продукты")

