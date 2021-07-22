from django.shortcuts import render
from django import forms
from django.http import HttpResponse
import random
from markdown2 import Markdown

from . import util

class wikiForm(forms.Form):
    title = forms.CharField(label="Title", widget=forms.TextInput())
    content = forms.CharField(label="Content", widget=forms.Textarea())

  

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def NewPage(request):
    if request.method == "POST":
        
        #title = request.POST.get('title')
        #content = request.POST.get('content')
        form = wikiForm(request.POST)
        
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
       
            entries = util.list_entries()
            for entry in entries:
                if entry.lower() == title.lower():
                    return render(request, "encyclopedia/EntryError.html")

            util.save_entry(title.lower(), content)
            markConvertion = Markdown()
            return render (request, "encyclopedia/entry.html" , {
                "title": title,
                "content": markConvertion.convert(content)
                })

        else:
            return render(request, "encyclopedia/EntryError.html")

    else:
        return render(request, "encyclopedia/NewPage.html", {
            "form": wikiForm()
        })


def wiki(request, title):
    #return HttpResponse(f"Hello, {title}")
    content = util.get_entry(title)
    if content == None:
        return render(request, "encyclopedia/EntryNotFound.html")

    else:
        markConvertion = Markdown()
        return render (request, "encyclopedia/entry.html" , {
            "title": title,
            "content": markConvertion.convert(content)
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

        data = {'title': title,
                'content': content}

        print("ok")
        return render (request, "encyclopedia/edit.html" , {
            'title': title,
            'content': content
            })
        #return render (request, "encyclopedia/edit.html" , {"form": wikiForm(data)})

#PENDIENTE  
def save(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    print(title)
    print(content)
    if title == None:
        title = "test"
    util.save_entry(title,content)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": content
        })

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
