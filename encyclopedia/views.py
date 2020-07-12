from django.shortcuts import render
import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    markdown = util.get_entry(entry)
    markdown_code = util.get_entry(entry)
    converted_code = markdown2.markdown(markdown_code)
    return render(request, 'encyclopedia/title.html', {'content' : converted_code }
    
)
def newpage(request):
    if request.method == "POST":
        header = request.POST.get("header")
        content = request.POST.get("content")
        try = util.get_entry(header)
        if test != None:
            messages.error(request,"This page already exists")
            return render(request, "encyclopedia/newpage.html", 
            "entries": util.list_entries()
            })

    else:
        util.save_entry(header,content)
        entry_new = util.get_entry(header)
        return redirect("/wiki/"+title)
else:
    header = ""
    content =""
    return render(request, "encyclopedia/newpage.html", 
            "entries": util.list_entries()
            })