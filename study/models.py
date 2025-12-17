from django.conf import settings
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название курса")
    image = models.ImageField(
        upload_to="study/courses/avatars",
        blank=True,
        null=True,
        verbose_name="Изображение курса",
    )
    description = models.TextField(verbose_name="Описание курса", blank=True, null=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Владелец",
        help_text="Укажите владельца",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название урока")
    image = models.ImageField(
        upload_to="study/lessons/avatars",
        blank=True,
        null=True,
        verbose_name="Изображение урока",
    )
    description = models.TextField(verbose_name="Описание урока", blank=True, null=True)
    video_url = models.URLField(max_length=200, verbose_name="Ссылка на видео")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Владелец",
        help_text="Укажите владельца",
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.title
