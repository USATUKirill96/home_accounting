from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .parser import Parser
from .serializer import Spending_Serializer
from .services import Db_Get, Db_Post, Db_Put


class SpendsView(APIView):
    """Defines views for requests associated with spendings."""
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
    """Defines views for requests associated with users."""
    def post(self, request):
        params = Parser.param_parse_post(request)
        print(params)
        Db_Post.create_database_user(**params)
        return Response('success')

    def put(self, request):
        params = Parser.param_parse_post(request)
        user = Db_Put.edit_messenger(**params)
        if user is not None:
            return Response('success')


class ValidateView(APIView):
    """Defines views for requests associated with validation."""
    def get(self, request):
        params = Parser.param_parse_get(request)
        result = Db_Get.validate_user(**params)
        return JsonResponse({"result": result})
