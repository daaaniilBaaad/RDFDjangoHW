from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from study.models import Course, Lesson
from study.validators import validate_words
from users.models import Followers


class LessonSerializer(serializers.ModelSerializer):
    video_url = serializers.URLField(required=False, validators=[validate_words])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):

    count_course_lesson = serializers.SerializerMethodField()
    lesson = LessonSerializer(source="lesson_set", many=True, read_only=True)
    is_subscribed = serializers.SerializerMethodField()

    def get_count_course_lesson(self, obj):
        return obj.lesson_set.count()

    class Meta:
        model = Course
        fields = "__all__"

    def get_is_subscribed(self, obj):
        """Проверяет подписан ли пользователь"""
        user = self.context.get("request").user
        if Followers.objects.filter(user=user, course=obj).exists():
            return "Подписан"
        else:
            return "Не подписан"