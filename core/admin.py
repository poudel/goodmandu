from django.contrib import admin
from core.models import (
    EntityType,
    Entity,
    ProjectType,
    ProjectStatus,
    Project,
    ProjectEvent,
    ProjectData
)


admin.site.register([
    EntityType,
    ProjectType,
    ProjectStatus,
])


class ProjectDataInline(admin.TabularInline):
    model = ProjectData


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ("slug", "created_by", "created_at", "modified_at")
    list_display = ("title", "type", "status", "url")
    inlines = [ProjectDataInline]

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user

        if obj.pk:
            is_create = False
        else:
            is_create = True

        super().save_model(request, obj, form, change)

        if is_create:
            ProjectEvent.objects.create(
                created_by=request.user,
                project=obj,
                title="Added {}".format(obj.title),
                description="Let this begin",
            )
        return obj


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "country",)
    readonly_fields = ("slug", "created_by", "created_at", "modified_at")


@admin.register(ProjectEvent)
class ProjectEventAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "url", "occurred_on",)
    readonly_fields = ("slug", "created_by", "created_at", "modified_at")

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user

        super().save_model(request, obj, form, change)
        return obj
