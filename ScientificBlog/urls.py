from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


# Include url pattern of ckeditor_uploader
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('Blog.urls'))
]

# if debug mode is True then project uses debug tool bar and including local media url and root
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls))
                  ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
