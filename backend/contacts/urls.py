from .views import ContactViewSet
from rest_framework.routers import DefaultRouter

app_name = 'contacts'

router = DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contacts')
urlpatterns = router.urls