from django.urls import path
from blog import views
# from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [

    path('', views.blog, name="Blog"),
    path('categoria/<int:categoria_id>/', views.catx, name="catx"),

]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
