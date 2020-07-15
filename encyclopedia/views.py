from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
import markdown2
import random
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    markdown = util.get_entry(entry)
    markdown_code = util.get_entry(entry)
    converted_code = markdown2.markdown(markdown_code)
    return render(request, 'encyclopedia/title.html', {'content' : converted_code,  "title": entry
        } 
    
)
def newpage(request):
    if request.method == "POST":
        header = request.POST.get("header")
        content = request.POST.get("content")
        test = util.get_entry(header)
        if test != None:
            messages.error(request,"This page already exists")
            return render(request, "encyclopedia/newpage.html", {
            "entries": util.list_entries()
            })

        else:
            util.save_entry(header,content)
            entry_new = util.get_entry(header)
            return redirect("/wiki/"+header)
    else:
        header = ""
        content =""
        return render(request, "encyclopedia/newpage.html", {
            "entries": util.list_entries()
            })


def random_page(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return redirect("/wiki/"+random_entry)

def error(request):
    return render(request, "encyclopedia/error.html", 
    )

def editpage1(request, title):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        util.save_entry(title,content)
        return redirect("/wiki/"+title)
    else:
        return render(request, "encyclopedia/editpage.html",{
        "title": entry
        })

def editpage2(request, title):
    title = request.POST.get("title")
    content = request.POST.get("content")
    header = util.get_entry(title)
    content = util.get_entry(entry)
    return render(request, "encyclopedia/editpage.html",{
        "header": title,
        "content": content
        })



def search(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    util.get_entry(title)
    return render(request, "encyclopedia/search.html", {
        "entries": util.list_entries()
    })
