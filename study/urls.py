from django.urls import path
from rest_framework.routers import SimpleRouter

from study.apps import StudyConfig
from study.views import (CourseViewSet, LessonCreateAPIView,
                         LessonDestroyAPIView, LessonListAPIView,
                         LessonRetrieveAPIView, LessonUpdateAPIView)

app_name = StudyConfig.name

router = SimpleRouter()
router.register("", CourseViewSet),

urlpatterns = [
    path("lesson/", LessonListAPIView.as_view(), name="lesson-list"),
    path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson-create"),
    path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson-get"),
    path(
        "lesson/update/<int:pk>/", LessonUpdateAPIView.as_view(), name="lesson-update"
    ),
    path(
        "lesson/delete/<int:pk>/", LessonDestroyAPIView.as_view(), name="lesson-delete"
    ),
]

urlpatterns += router.urls
