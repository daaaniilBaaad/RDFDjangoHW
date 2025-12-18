from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from users.models import Payments, User, Followers


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = "__all__"


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class FollowSerializer(ModelSerializer):

    class Meta:
        model = Followers
        fields = "__all__"