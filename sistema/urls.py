from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('love_story.urls')),  # Asegúrate de que esto apunta a tu aplicación
    path('accounts/', include('django.contrib.auth.urls')),  # Para la autenticación
]



