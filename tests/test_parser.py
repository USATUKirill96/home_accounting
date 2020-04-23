from django.test import TestCase
from dbapi.parser import notice_user
from dbapi.services import Db_Post
from dbapi.models import DbUser


class ParseMethods(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        Db_Post.create_database_user(user_id=22)

    def test_create_db_user(self):
        user1 = DbUser.objects.get(site_id=22)
        user2 = notice_user(user_id=22, source='site')
        self.assertEqual(user1, user2)
