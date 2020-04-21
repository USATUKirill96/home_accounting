from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from django.http import JsonResponse
from .serializer import Spending_Serializer
from .services import Db_Get, Db_Post, Db_Put
from .api import Parser


# Create your views here.


class SpendsView(APIView):
    def get(self, request):
        params = Parser.param_parse_get(request)
        elements = Db_Get.get_spends(**params)
        serializer = Spending_Serializer(elements, many=True)
        return JsonResponse({"Spendings": serializer.data})

    def post(self, request):
        params = Parser.param_parse_post(request)
        Db_Post.create_spending(**params)
        return Response('vrode vse')


class UsersView(APIView):
    def post(self, request):
        params = Parser.param_parse_post(request)
        print(params)
        Db_Post.create_database_user(**params)
        return Response('success')

    def put(self, request):
        params = Parser.param_parse_post(request)
        user = Db_Put.add_messenger(**params)
        if user is not None:
            return Response('success')


class ValidateView(APIView):
    def get(self, request):
        params = Parser.param_parse_get(request)
        result = Db_Get.validate_user(**params)
        return JsonResponse({"result": result})
