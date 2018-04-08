from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from core import apis


router = DefaultRouter()
router.register("entity", apis.EntityAPI)
router.register("entity-type", apis.EntityTypeAPI)
router.register("project", apis.ProjectAPI)
router.register("project-type", apis.ProjectTypeAPI)
router.register("project-event", apis.ProjectEventAPI)


urlpatterns = [
    path("api/token/", views.obtain_auth_token),
    path("api/", include(router.urls))
]
