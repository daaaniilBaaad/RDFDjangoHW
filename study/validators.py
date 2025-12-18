from rest_framework.serializers import ValidationError


def validate_words(value):
    """ Проверка на отсутствие ссылок на сторонние ресурсы. """
    if "youtube.com" not in value:
        raise ValidationError("Разрешены ссылки только на youtube.com")