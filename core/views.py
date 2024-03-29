from django.shortcuts import render
from django.views import View

# Create your views here.

class index_view(View):

    def __init__(self, *args, **kwargs):
        self.template_name = "core/index.html"
        print("Index view initialised.")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[""] = {}
        return context
    
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)