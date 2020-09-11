from django.conf.urls import url, include
from django.contrib import admin

# used to images
from django.conf import settings
from django.conf.urls.static import static

# used to rest_framework route
from api.views import PicturesViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'pictures', PicturesViewSet, 'pictures')

# another form
# from rest_framework.urlpatterns import format_suffix_patterns
# from api import views

# used to call route
urlpatterns = [
    url(r'^ws/', include(router.urls)),
    # url(r'^ws/pictures/', views.PicturesList.as_view()),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # used to images
