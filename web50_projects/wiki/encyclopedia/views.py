from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
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

        entries = util.list_entries(True)

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

def search(request):
    if request.method == 'POST':
        query = (request.POST['query']).lower() # get the value of query string

        entries = util.list_entries(True)

        if query in entries:
            return HttpResponseRedirect(reverse('wiki', args = (query,)))
        else:
            # get a list of entries that has query as a substring in its name
            entries = util.list_matching_entries(query)

            if not entries:  # if entries is empty (no entries matched with the query)
                raise Http404(f"No entries found for input query '{query}'")
            else:
                return render(request, 'encyclopedia/search.html', {'entries': entries, 'query': query})
            





