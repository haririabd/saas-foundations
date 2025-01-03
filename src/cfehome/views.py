import pathlib
from django.shortcuts import render
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def index_view(request, *args, **kwargs):
    page_title = "Homepage"
    html_template = "index.html"
    qs = PageVisit.objects.all().count()
    q = PageVisit.objects.filter(path=request.path).count()

    context = {
        "page_title": page_title,
        "total_visit": qs,
        "page_visit": q
    }
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, context)

def about_view(request, *args, **kwargs):
    return index_view(request, *args, **kwargs)