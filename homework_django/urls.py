from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import ads.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ads/', include("ads.urls")),
    path('cat/', include("category.urls")),
    path('user/', include("users.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
