from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("allauth.urls")),
    path('', include('city_voting_registration.urls')),
    path('', include('city_map.urls')),
    path('', include('homepage.urls')),
    path('polls/', include('voting.urls')),
]
