from django.urls import path
from .views import general, me, contact

urlpatterns = [
   path('', general),
   path('me', me),
   path('contact', contact),
]