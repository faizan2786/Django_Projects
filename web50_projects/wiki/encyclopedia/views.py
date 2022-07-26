from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render
import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wiki(request, entry_name):
    if request.method=='GET':

        # get the entry content from list of entries
        # return error if entry doesn't exist

        entries = util.list_entries()
        entries = [e.lower() for e in entries]

        if entry_name.lower() not in entries:
            raise Http404(f"Requested wikipedia entry '{entry_name}' not found!")
        else:
            # get the entry content (in markdown format) and convert it to the html response
            
            entry_content = util.get_entry(entry_name.title())
            entry_content_html = markdown2.markdown(entry_content)
            args = {
                    'entry_name': entry_name.title(),
                    'entry_content': entry_content_html
                    }

            return render(request, 'encyclopedia/wiki.html', args);  

