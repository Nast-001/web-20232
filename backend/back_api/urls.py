from django.contrib import admin
from django.urls import path, include
from routers import router
from course.views import CourseViewSet
from django.conf.urls.static import static
from django.conf import settings

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

schema_view = swagger_get_schema_view(
    openapi.Info(
        title='API',
        default_version='1.0.0',
        description='API documentation',
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((router.urls, 'courses'), namespace='courses')),
    path('api/', include((router.urls, 'mailingList'), namespace='mailingList')),
    path('api/', include((router.urls, 'members'), namespace='members')),
    path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
