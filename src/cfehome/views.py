from django.shortcuts import render

def index_view(request, *args, **kwargs):
    template_name = 'index.html',
    context = {}
    return render(request, template_name, context)