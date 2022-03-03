from django.urls import path
from django.views.generic import TemplateView
from .views import ContactViewSet
from rest_framework.routers import DefaultRouter

app_name = 'contacts'

router = DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contact')
urlpatterns = router.urls