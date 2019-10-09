from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import (
    EntityType,
    Entity,
    ProjectType,
    ProjectStatus,
    Project,
    ProjectEvent,
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
        fields = ("id", "name")


class EntitySerializer(serializers.ModelSerializer):
    type = EntityTypeSerializer(read_only=True)
    country = serializers.SerializerMethodField()

    def get_country(self, entity):
        return entity.country.name if entity.country else None

    class Meta:
        model = Entity
        fields = ("id", "name", "type", "country", "url")


class ProjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectType
        fields = ("id", "name")


class ProjectStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStatus
        fields = ("id", "name")


class ProjectBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "title")


class ProjectSerializer(serializers.ModelSerializer):
    backers = EntitySerializer(many=True, read_only=True)
    contractors = EntitySerializer(many=True, read_only=True)
    type = ProjectTypeSerializer(read_only=True)
    status = ProjectStatusSerializer(read_only=True)

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "type",
            "status",
            "backers",
            "contractors",
        )


class ProjectEventSerializer(serializers.ModelSerializer):
    project = ProjectBasicSerializer(read_only=True)

    class Meta:
        model = ProjectEvent
        fields = ("id", "project", "url", "title", "description", "occurred_on")
