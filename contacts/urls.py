from django.urls import path
from django.views.generic import TemplateView
from .views import ContactListView, ContactCreateView, ContactUpdateView, ContactDeleteView


app_name = 'contacts'

urlpatterns = [
    path('', TemplateView.as_view(template_name='contacts/index.html')),
    path('contacts/', ContactListView.as_view(), name='all'),
    path('contacts/create/', ContactCreateView.as_view(), name='contact_create'),
    
    # <int:pk> signifies the id of the contact book entry 
    path('contacts/<int:pk>/update/', ContactUpdateView.as_view(), name='contact_update'), 
    path('contacts/<int:pk>/delete/', ContactDeleteView.as_view(), name='contact_delete'),
]