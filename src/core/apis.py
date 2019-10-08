from rest_framework.viewsets import ReadOnlyModelViewSet
from core.models import EntityType, Entity, ProjectType, ProjectStatus, Project, ProjectEvent
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
    queryset = Entity.objects.select_related("type", "created_by").order_by('-id')
    serializer_class = EntitySerializer
    ordering_fields = ['id']


class ProjectTypeAPI(ReadOnlyModelViewSet):
    queryset = ProjectType.objects.all()
    serializer_class = ProjectTypeSerializer


class ProjectStatusAPI(ReadOnlyModelViewSet):
    queryset = ProjectStatus.objects.all()
    serializer_class = ProjectStatusSerializer


class ProjectAPI(ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer
    ordering_fields = ['id']
    queryset = (
        Project.objects.select_related("type", "status", "created_by")
        .prefetch_related("backers", "contractors", "extra_data")
        .order_by('-id')
    )


class ProjectEventAPI(ReadOnlyModelViewSet):
    queryset = ProjectEvent.objects.select_related("project").order_by('-id')
    serializer_class = ProjectEventSerializer
    ordering_fields = ['id']
