from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from core import apis, views


router = DefaultRouter()
router.register("entity", apis.EntityAPI)
router.register("entity-type", apis.EntityTypeAPI)
router.register("project", apis.ProjectAPI)
router.register("project-type", apis.ProjectTypeAPI)
router.register("project-status", apis.ProjectStatusAPI)
router.register("project-event", apis.ProjectEventAPI)


view_patterns = ([
    path("project/",
         views.ProjectList.as_view(),
         name="project-list"),
    path("project/<slug:slug>/",
         views.ProjectDetail.as_view(),
         name="project-detail"
    ),
    path("project/event/<slug:slug>/",
         views.ProjectEventDetail.as_view(),
         name="project-event-detail"),
], "core")


urlpatterns = [
    path("api/token/", obtain_auth_token),
    path("api/", include(router.urls)),
    path("", include(view_patterns)),
]
