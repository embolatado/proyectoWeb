from django.urls import path
from webBlog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name="Home"),
    path('servicios', views.servicios, name="Servicios"),
    path('tienda', views.tienda, name="Tienda"),
    path('blog', views.blog, name="Blog"),
    path('contacto', views.contacto, name="Contacto"),
]
