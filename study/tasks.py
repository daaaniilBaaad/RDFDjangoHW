from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from celery import shared_task

from users.models import User


@shared_task
def send_information(email):
    """Отправляет сообщение пользователю об обновлении материалов курса."""
    send_mail('Обновление материала', 'Вышло новое обновление', EMAIL_HOST_USER, [email])


@shared_task
def time_block_user():
    """Проверяет и блокирует неактивных пользователей"""
    User.objects.filter(
        last_login__lt=timezone.now() - timezone.timedelta(days=30), is_active=True
    ).update(is_active=False)
    print()