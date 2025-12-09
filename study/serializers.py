from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from study.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

    count_course_lesson = serializers.SerializerMethodField()
    lesson = LessonSerializer(source='lesson_set', many=True)

    def get_count_course_lesson(self, obj):
        return obj.lesson_set.count()

    class Meta:
        model = Course
        fields = '__all__'
