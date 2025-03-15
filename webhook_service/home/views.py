from django.shortcuts import render

from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    AccountSerializer,
    DestinationSerializer,
    AccountMemberSerializer,
)


class WebhookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]


def home(request):
    return HttpResponse("<h1>Welcome to the Webhook Service API</h1>")


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]


class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes = [IsAuthenticated]


class AccountMemberViewSet(viewsets.ModelViewSet):
    queryset = AccountMember.objects.all()
    serializer_class = AccountMemberSerializer
    permission_classes = [IsAuthenticated]


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
            )
        else:
            return Response({"error": "Invalid credentials"}, status=400)
