from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from core.models import (
    EntityType,
    Entity,
    ProjectType,
    ProjectStatus,
    Project,
    ProjectEvent,
)
from core.serializers import (
    EntityTypeSerializer,
    EntitySerializer,
    ProjectTypeSerializer,
    ProjectStatusSerializer,
    ProjectSerializer,
    ProjectEventSerializer,
)


class EntityTypeAPI(ReadOnlyModelViewSet):
    queryset = EntityType.objects.all()
    serializer_class = EntityTypeSerializer


class EntityAPI(ReadOnlyModelViewSet):
    queryset = Entity.objects.select_related("type", "created_by").all()
    serializer_class = EntitySerializer


class ProjectTypeAPI(ReadOnlyModelViewSet):
    queryset = ProjectType.objects.all()
    serializer_class = ProjectTypeSerializer


class ProjectStatusAPI(ReadOnlyModelViewSet):
    queryset = ProjectStatus.objects.all()
    serializer_class = ProjectStatusSerializer


class ProjectAPI(ReadOnlyModelViewSet):
    queryset = Project.objects.select_related("type", "status", "created_by")\
                              .prefetch_related("backers", "contractors").all()
    serializer_class = ProjectSerializer


class ProjectEventAPI(ReadOnlyModelViewSet):
    queryset = ProjectEvent.objects.select_related("project").all()
    serializer_class = ProjectEventSerializer
