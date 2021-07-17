from django.shortcuts import render
from django import forms
from django.http import HttpResponse
import random

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

        util.save_entry(title.lower(), content)

        return render(request, "encyclopedia/index.html")

    else:
        return render(request, "encyclopedia/NewPage.html")


def wiki(request, title):
    #return HttpResponse(f"Hello, {title}")
    content = util.get_entry(title)
    if content == None:
        return render(request, "encyclopedia/EntryNotFound.html")

    else:
        return render (request, "encyclopedia/entry.html" , {
            "title": title,
            "content": content
            })

def search(request):
    if request.method =="POST":

        parcialMatch = []
        title = request.POST.get('q')
        entries = util.list_entries()

        for entry in entries:
            if entry.lower() == title.lower():
                return render (request, "encyclopedia/entry.html" , {
                "title": title.capitalize(),
                "content": util.get_entry(title)
                })
            elif entry.find(title) != -1:
                parcialMatch.append(entry)
        
        return render(request, "encyclopedia/searchResults.html", {
        "entries": parcialMatch,
        "number" : len(parcialMatch)
    })

def edit(request, title):
    if request.method == "GET":
        content = util.get_entry(title)
        print("ok")

        return render (request, "encyclopedia/edit.html" , {
            "title": title,
            "content": content
                })
#PENDIENTE  
def save(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    print(title)
    print("almost done")
    return render(request, "encyclopedia/index.html")

def randomPage(request):
    entries = util.list_entries()
    lenght = len(entries)
    entry_show = random.randint(0, lenght)

    title = entries[entry_show]
    content = util.get_entry(title)

    return render (request, "encyclopedia/entry.html" , {
        "title": title,
        "content": content
        })
