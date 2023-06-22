from rest_framework import viewsets
from course.models import Course
from course.serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    def get_queryset(self):
        return Course.objects.all()
