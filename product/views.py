from typing import Any
from django.shortcuts import render
from django.views import View

# Create your views here.

class product_detail_view(View):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.template_name = "product/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[""] = {}
        return context
    
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)