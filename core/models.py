from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class EntityType(BaseModel):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("created by"),
        null=True,
        on_delete=models.CASCADE
    )
    name = models.CharField(_("name"), max_length=100, unique=True)

    def __str__(self):
        return self.name


class Entity(BaseModel):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("created by"),
        null=True,
        on_delete=models.CASCADE
    )
    name = models.CharField(_("name"), max_length=200, unique=True)
    type = models.ForeignKey(
        EntityType,
        verbose_name=_("type"),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class ProjectType(BaseModel):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("created by"),
        null=True,
        on_delete=models.CASCADE
    )
    name = models.CharField(_("name"), max_length=100, unique=True)

    def __str__(self):
        return self.name


class Project(BaseModel):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("created by"),
        null=True,
        on_delete=models.CASCADE
    )
    name = models.CharField(_("name"), max_length=200, unique=True)
    backers = models.ManyToManyField(
        Entity,
        verbose_name=_("backers"),
        blank=True,
        related_name="backed_projects"
    )
    contractors = models.ManyToManyField(
        Entity,
        verbose_name=_("contractors"),
        blank=True,
        related_name="contracted_projects"
    )

    type = models.ForeignKey(
        ProjectType,
        verbose_name=_("type"),
        on_delete=models.CASCADE
    )

    start_year = models.PositiveSmallIntegerField(
        _("start year"),
        null=True,
        blank=True
    )
    start_month = models.PositiveSmallIntegerField(
        _("start month"),
        null=True,
        blank=True
    )

    end_year = models.PositiveSmallIntegerField(
        _("estimated end year"),
        null=True,
        blank=True
    )
    end_month = models.PositiveSmallIntegerField(
        _("estimated end month"),
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class ProjectEvent(BaseModel):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("created by"),
        null=True,
        on_delete=models.CASCADE
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="events",
        verbose_name=_("project")
    )
    title = models.CharField(_("title"), max_length=300)
    description = models.TextField(_("description"), blank=True)
    occured_on = models.DateField(_("occured on"), null=True, blank=True)

    def __str__(self):
        return self.title
