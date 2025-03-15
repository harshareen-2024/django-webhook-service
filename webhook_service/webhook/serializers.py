from rest_framework import serializers
from .models import Webhook
from .models import Account
from .models import Destination, AccountMember, Account, Webhook


class WebhookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webhook
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = "__all__"


class AccountMemberSerializer(serializers.ModelSerializer):  # ✅ Add this if missing
    class Meta:
        model = AccountMember
        fields = "__all__"
