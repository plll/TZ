from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')), 
    path('admin/', admin.site.urls),
    path('', include('bank.urls', namespace='app_bank'))
]
