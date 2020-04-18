from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import Spending_Serializer
from .services import notice_user, Db_Get


# Create your views here.

class GetView(APIView):
    def get(self, request):
        id = request.GET.get('id')
        source = request.GET.get('source')
        user = notice_user(id, source)
        if user is None:
            return "Такого пользователя не существует"
        elements = Db_Get.get_spends(user)
        serializer = Spending_Serializer(elements, many=True)
        return Response({"Spendings": serializer.data})
