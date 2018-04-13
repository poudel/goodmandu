import calendar
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField
from core.utils import get_random_string, slugify


class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class SlugModel(BaseModel):
    SLUG_BASE_FIELD = "title"
    slug = models.SlugField(_("slug"), unique=True, editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_base = getattr(self, self.SLUG_BASE_FIELD)
            slug = slugify(slug_base + " " + get_random_string(6, uppercase=False))
            while self.__class__.objects.filter(slug=slug).exists():
                slug = slugify(slug_base + " " + get_random_string(6, uppercase=False))
            self.slug = slug
        return super().save(*args, **kwargs)


class EntityType(BaseModel):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("created by"),
        null=True,
        editable=False,
        on_delete=models.CASCADE
    )
    name = models.CharField(_("name"), max_length=100, unique=True)

    class Meta:
        verbose_name = _("entity type")
        verbose_name_plural = _("entity types")

    def __str__(self):
        return self.name


class Entity(SlugModel):
    SLUG_BASE_FIELD = "name"
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("created by"),
        null=True,
        editable=False,
        on_delete=models.CASCADE
    )
    name = models.CharField(_("name"), max_length=200, unique=True)
    type = models.ForeignKey(
        EntityType,
        verbose_name=_("type"),
        on_delete=models.CASCADE
    )
    country = CountryField()

    class Meta:
        verbose_name = _("entity")
        verbose_name_plural = _("entities")

    def __str__(self):
        return self.name


class ProjectType(BaseModel):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("created by"),
        null=True,
        editable=False,
        on_delete=models.CASCADE
    )
    name = models.CharField(_("name"), max_length=100, unique=True)

    class Meta:
        verbose_name = _("project type")
        verbose_name_plural = _("project types")

    def __str__(self):
        return self.name


class ProjectStatus(BaseModel):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("created by"),
        null=True,
        editable=False,
        on_delete=models.CASCADE
    )
    name = models.CharField(_("name"), max_length=100, unique=True)

    class Meta:
        verbose_name = _("project status")
        verbose_name_plural = _("project status")

    def __str__(self):
        return self.name


class Project(SlugModel):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("created by"),
        null=True,
        editable=False,
        on_delete=models.CASCADE
    )
    title = models.CharField(_("title"), max_length=200, unique=True)
    description = models.TextField(_("description"), blank=True)
    url = models.URLField(_("url"), max_length=300, blank=True)
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
    status = models.ForeignKey(
        ProjectStatus,
        verbose_name=_("status"),
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
    completion = models.IntegerField(
        _("estimated completion percentage"),
        null=True,
        blank=True,
        editable=False
    )

    class Meta:
        verbose_name = _("project")
        verbose_name_plural = _("projects")

    def __str__(self):
        return self.title

    def get_basic_info(self):
        return {"id": self.id, "title": self.title}

    def join_year_month(self, year, month):
        s = []
        if year:
            s.append(str(year))
        else:
            return

        if month:
            s.insert(0, calendar.month_name[month])
        return ", ".join(s)

    @property
    def start(self):
        return self.join_year_month(self.start_year, self.start_month)

    @property
    def end(self):
        return self.join_year_month(self.end_year, self.end_month)


class ProjectData(BaseModel):
    # to store extra data about a project
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="extra_data",
        verbose_name=_("project")
    )
    key = models.CharField(
        _("key"),
        max_length=50
    )
    value = models.CharField(
        _("value"),
        max_length=500
    )

    class Meta:
        verbose_name = _("project data")
        verbose_name_plural = _("project data")

    def __str__(self):
        return "{} - {}".format(self.key, self.value)


class ProjectEvent(SlugModel):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("created by"),
        null=True,
        editable=False,
        on_delete=models.CASCADE
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="events",
        verbose_name=_("project")
    )
    url = models.URLField(_("url"), max_length=300, blank=True)
    title = models.CharField(_("title"), max_length=300)
    description = models.TextField(_("description"), blank=True)
    occurred_on = models.DateField(_("occurred on"), null=True, blank=True)

    class Meta:
        verbose_name = _("project event")
        verbose_name_plural = _("project events")

    def __str__(self):
        return self.title


# class EmailSubscription(BaseModel):
#     email = models.EmailField(unique=True)
#     is_active = models.BooleanField(default=False)

#     def __str__(self):
#         return self.email
