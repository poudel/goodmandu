from django.contrib import admin
from core.models import (
    EntityType,
    Entity,
    ProjectType,
    Project,
    ProjectEvent
)


admin.site.register([
    EntityType,
    Entity,
    ProjectType,
    Project,
    ProjectEvent,
])
