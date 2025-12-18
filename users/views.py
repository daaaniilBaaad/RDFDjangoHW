from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, UpdateAPIView, get_object_or_404)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from study.models import Course
from users.models import Payments, User, Followers
from users.serializers import PaymentSerializer, UserSerializer, FollowSerializer


class PaymentViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentSerializer
    """Настройка фильтрации"""
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["pay_method", "paid_lesson", "paid_course"]
    ordering_fields = ["pay_date"]


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class FollowersView(APIView):
    queryset = Followers.objects.all()
    serializer_class = FollowSerializer

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get("id")
        course_item = get_object_or_404(Course, id=course_id)
        subs_item = Followers.objects.filter(user=user, courses=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = "Подписка удалена"
            status_code = status.HTTP_200_OK
        else:
            Followers.objects.create(user=user, courses=course_item)
            message = "Подписка добавлена"
            status_code = status.HTTP_201_CREATED

        return Response({"message": message}, status=status_code)
