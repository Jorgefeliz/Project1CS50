from django.shortcuts import render
from django import forms
from django.http import HttpResponse

from . import util

class wikiForm(forms.Form):
    title = forms.CharField(label="Title")
  

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def NewPage(request):
    if request.method == "POST":
        
        title = request.POST.get('title')
        content = request.POST.get('content')
        #form = wikiForm(request.POST)
        
        #if form.is_valid():
          #  title = form.cleaned_data["Title"]
       
        entries = util.list_entries()
        for entry in entries:
            if entry.lower() == title.lower():
                return render(request, "encyclopedia/EntryError.html")

        util.save_entry(title, content)

        return render(request, "encyclopedia/index.html")

    else:
        return render(request, "encyclopedia/NewPage.html")


def wiki(request, title):
    return HttpResponse("Hello, {title}")
    