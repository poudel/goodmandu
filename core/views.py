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

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')

        if q:
            qs = qs.filter(title__icontains=q)
        return qs.order_by('-id')


class ProjectDetail(DetailView):
    model = Project


class ProjectEventDetail(DetailView):
    model = ProjectEvent
