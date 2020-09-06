from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('registry/', include('app.urls')),
    path('admin/', admin.site.urls),
]
