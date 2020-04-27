from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .parser import Parser
from .serializer import Spending_Serializer, Incomes_Serializer
from .services import Db_Get, Db_Post, Db_Put, Db_Delete


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

    def put(self, request):
        params = Parser.param_parse_post(request)
        result = Db_Put.edit_spending(**params)
        return Response(result)

    def delete(self, request):
        params = Parser.param_parse_get(request)
        Db_Delete.delete_spending(**params)
        return True


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


class IncomesView(APIView):
    """Defines views for requests associated with incomes operation."""

    def get(self, request):
        data = Parser.param_parse_get(request)
        result = Db_Get.get_incomes(**data)
        serializer = Incomes_Serializer(result, many=True)
        return JsonResponse({'Incomes': serializer.data})

    def post(self, request):
        data = Parser.param_parse_post(request)
        result = Db_Post.create_income(**data)
        return JsonResponse({"result": result})

    def put(self, request):
        data = Parser.param_parse_post(request)
        result = Db_Put.edit_income(**data)
        return JsonResponse({"result": result})

    def delete(self, request):
        data = Parser.param_parse_get(request)
        result = Db_Delete.delete_income(**data)
        return JsonResponse({"result": result})
