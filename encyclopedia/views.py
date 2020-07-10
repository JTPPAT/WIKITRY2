from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    markdown = util.get_entry(entry)
    return render(request, 'encyclopedia/title.html', {'content' : markdown}
)
def newpage(request):
    return render(request, "encyclopedia/newpage.html", {
            })

