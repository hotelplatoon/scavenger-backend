from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include

urlpatterns = [
    url('admin/', admin.site.urls),
    url('api/', include('hunt_app.urls'))
]