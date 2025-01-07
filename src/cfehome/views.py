import pathlib
from django.shortcuts import render
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def Index(request, *args, **kwargs):
    page_title = 'Homepage'
    html_template = 'index.html'

    # page visit need to redesign in visits.view so it can be re-use
    # now, only index view have the page visit counter
    # need to consider the database size also
    qs = PageVisit.objects.all().count()
    q = PageVisit.objects.filter(path=request.path).count()

    context = {
        "page_title": page_title,
        "total_visit": qs,
        "page_visit": q
    }
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, context)

def About(request, *args, **kwargs):
    page_title = 'About'
    html_template = 'about.html'

    context = {
        "page_title": page_title
    }
    return render(request, html_template, context)

def Contact(request, *args, **kwargs):
    page_title = 'Contact'
    html_template = 'contact.html'

    context = {
        "page_title": page_title
    }
    return render(request, html_template, context)