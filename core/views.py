from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from core.models import Project, ProjectEvent


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['projects'] = Project.objects.order_by("-id")[:20]
        ctx['events'] = ProjectEvent.objects.order_by("-id")[:50]
        return ctx


class ProjectList(ListView):
    model = Project
    paginate_by = 25

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')

        if q is not None and len(q) > 3:
            qs = qs.filter(title__icontains=q)
        return qs.order_by('-id')


class ProjectDetail(DetailView):
    model = Project


class ProjectEventList(ListView):
    model = ProjectEvent
    paginate_by = 25

    def get_queryset(self):
        qs = super().get_queryset()
        project_id = self.request.GET.get('project')

        if project_id and project_id.isnumeric():
            self.project = Project.objects.get(id=project_id)
            qs = qs.filter(project=self.project)
        else:
            self.project = None
        return qs.order_by('-id')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        ctx['project'] = self.project
        return ctx


class ProjectEventDetail(DetailView):
    model = ProjectEvent
