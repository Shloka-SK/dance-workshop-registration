from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    # Dance workshop application
    path('', include('dance_styles.urls')),

    # Chatbot
    path('chatbot/', include('chatbot.urls')),
]


# Serve uploaded media files
# Required for the images used by the dance workshop.
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)