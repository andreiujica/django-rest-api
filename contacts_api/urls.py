from django.urls import path
from .views import ContactListView, ContactCreateView, ContactUpdateView, ContactDeleteView

app_name = 'contacts_api'

# define urls for the 4 CRUD-based pages and link them with a view
urlpatterns = [
    path('contacts/', ContactListView.as_view(), name='all'),
    path('contacts/create/', ContactCreateView.as_view(), name='contact_create'),
    
    # <int:pk> signifies the id of the contact book entry 
    path('contacts/<int:pk>/update/', ContactUpdateView.as_view(), name='contact_update'), 
    path('contacts/<int:pk>/delete/', ContactDeleteView.as_view(), name='contact_delete'),
]