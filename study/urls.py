from django.urls import path
from rest_framework.routers import SimpleRouter

from study.views import CourseViewSet, LessonListAPIView, LessonCreateAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIViewAPIView
from study.apps import StudyConfig

app_name = StudyConfig.name

router = SimpleRouter()
router.register('', CourseViewSet),

urlpatterns = [
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIViewAPIView.as_view(), name='lesson-delete'),
]

urlpatterns += router.urls