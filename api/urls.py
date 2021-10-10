from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from objective_harmony import views

router = routers.DefaultRouter()
router.register(r"spectrums", views.SpectrumView, "spectrum")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
