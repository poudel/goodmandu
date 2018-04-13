from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import (
    EntityType,
    Entity,
    ProjectType,
    ProjectStatus,
    Project,
    ProjectEvent
)


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, user):
        return user.get_full_name()

    class Meta:
        model = User
        fields = ("username", "name")


class EntityTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EntityType
        fields = ("id", "name",)


class CreatedByModelSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    def create(self, data):
        data["created_by"] = self.context["request"].user
        return super().create(data)


class EntitySerializer(CreatedByModelSerializer):
    type = EntityTypeSerializer(read_only=True)

    class Meta:
        model = Entity
        fields = ("id", "name", "created_by", "type")


class ProjectTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectType
        fields = ("id", "name",)


class ProjectStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectStatus
        fields = ("id", "name",)


class ProjectBasicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = (
            "id",
            "name",
        )


class ProjectSerializer(CreatedByModelSerializer):
    backers = EntitySerializer(many=True, read_only=True)
    contractors = EntitySerializer(many=True, read_only=True)
    type = ProjectTypeSerializer(read_only=True)
    status = ProjectStatusSerializer(read_only=True)

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "start_year",
            "start_month",
            "end_year",
            "end_month",
            "type",
            "status",
            "created_by",
            "backers",
            "contractors",
        )


class ProjectEventSerializer(CreatedByModelSerializer):
    project = ProjectBasicSerializer(read_only=True)

    class Meta:
        model = ProjectEvent
        fields = (
            "id",
            "created_by",
            "project",
            "url",
            "title",
            "description",
            "occurred_on"
        )
