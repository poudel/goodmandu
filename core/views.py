from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import Project, ProjectEvent


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['projects'] = Project.objects.order_by("-id")[:10]
        ctx['events'] = ProjectEvent.objects.order_by("-id")[:50]
        return ctx
