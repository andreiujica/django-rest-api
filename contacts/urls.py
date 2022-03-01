from django.urls import path
from django.views.generic import TemplateView

app_name = 'contacts'

url_patterns = [
    path('', TemplateView.as_view(template_name='contacts/index.html'))
]