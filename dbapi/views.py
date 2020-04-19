from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from django.http import JsonResponse
from .serializer import Spending_Serializer
from .services import notice_user, Db_Get, Db_Post, Db_Put


# Create your views here.


class SpendsView(APIView):
    def get(self, request):
        user = notice_user(request)
        if user is None:
            return JsonResponse({"status":404})
        elements = Db_Get.get_spends(user)
        serializer = Spending_Serializer(elements, many=True)
        return JsonResponse({"Spendings": serializer.data})

    def post(self, request):
        Db_Post.create_spending(request)
        return Response('vrode vse')


class UsersView(APIView):
    def post(self, request):
        Db_Post.create_database_user(request)
        return Response('success')


    def put(self, request):
        user = Db_Put.add_messenger(request)
        if user is not None:
            return Response('success')


