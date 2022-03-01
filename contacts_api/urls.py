from django.urls import path
from views import ContactListView, ContactCreateView, ContactUpdateView, ContactDeleteView

app_name = 'contacts_api'

url_patterns = [
    path('', ContactListView.as_view(), name='all'),
    path('contacts/create/', ContactCreateView.as_view(), name='contact_create'),
    path('contacts/<int:pk>/update/', ContactUpdateView.as_view(), name='contact_update'),
    path('contacts/<int:pk>/delete/', ContactDeleteView.as_view(), name='contact_delete'),
]