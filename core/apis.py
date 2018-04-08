from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from core.models import (
    EntityType,
    Entity,
    ProjectType,
    Project,
    ProjectEvent
)
from core.serializers import (
    EntityTypeSerializer,
    EntitySerializer,
    ProjectTypeSerializer,
    ProjectSerializer,
    ProjectEventSerializer,
)


class BaseAPIMixin:
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)


class EntityTypeAPI(BaseAPIMixin, ModelViewSet):
    queryset = EntityType.objects.all()
    serializer_class = EntityTypeSerializer


class EntityAPI(BaseAPIMixin, ModelViewSet):
    queryset = Entity.objects.select_related("type", "created_by").all()
    serializer_class = EntitySerializer


class ProjectTypeAPI(BaseAPIMixin, ModelViewSet):
    queryset = ProjectType.objects.all()
    serializer_class = ProjectTypeSerializer


class ProjectAPI(BaseAPIMixin, ModelViewSet):
    queryset = Project.objects.select_related("type", "created_by")\
                              .prefetch_related("backers", "contractors").all()
    serializer_class = ProjectSerializer


class ProjectEventAPI(ModelViewSet):
    queryset = ProjectEvent.objects.all()
    serializer_class = ProjectEventSerializer
