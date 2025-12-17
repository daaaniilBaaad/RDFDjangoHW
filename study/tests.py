from django.db.models.expressions import result
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from study.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="")
        self.course = Course.objects.create(title="Первый курс")
        self.lesson = Lesson.objects.create(title="Урок", course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrive(self):
        """Тест на статус и просмотр урока"""
        url = reverse('study:lesson-get', args=[self.lesson.pk,])
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('title'), "Урок")

    def test_lesson_create(self):
        """Тест на создание урока"""
        url = reverse('study:lesson-create')
        # self.course = Course.objects.create(title="Первый курс")
        data = {
            "title": "Урок",
            "course": 1
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.count(), 2)

    def test_lesson_update(self):
        """Тест на обновление урока"""
        url = reverse('study:lesson-update', args=[self.lesson.pk,])
        data = {
            "title": "Урок"
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('title'), "Урок")

    def test_lesson_delete(self):
        """Тест на удаление урока"""
        url = reverse('study:lesson-delete', args=[self.lesson.pk,])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        """Тест на список уроков"""
        url = reverse('study:lesson-list')
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "video_url": "",
                    "title": self.lesson.title,
                    "description": None,
                    "image": None,
                    "course": self.course.pk,
                    "owner": self.user.pk
                }
            ]}
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_subscribe_course(self):
        """Тест на подписку на курс"""
        url = reverse("users:followers-view")
        data = {
            "id": self.course.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get("message"), "Подписка добавлена")
        response = self.client.post(url, data)
        self.assertEqual(response.data.get("message"), "Подписка удалена")
