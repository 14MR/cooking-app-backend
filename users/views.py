from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserSerializer


class ProfileAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = {"id": request.user.id, **request.data}
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(id=request.user.id)
        serializer.update(instance=user, validated_data=serializer.validated_data)

        response = UserSerializer(user).data

        return JsonResponse(response)

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
