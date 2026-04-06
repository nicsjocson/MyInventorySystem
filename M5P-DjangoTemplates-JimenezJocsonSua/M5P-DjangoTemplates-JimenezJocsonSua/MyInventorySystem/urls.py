from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Change 'admin.site.pk' to 'admin.site.urls'
    path('admin/', admin.site.urls),
    
    # This line tells Django to look at your App's URLs
    path('', include('MyInventoryApp.urls')), 
]