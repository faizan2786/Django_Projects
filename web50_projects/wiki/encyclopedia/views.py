import random
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from numpy import tile


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
            return render_entry_page(request, entry_name)
          
def search(request):
    """
    getting a post request on this method will either render the requested page if an exact entry is found
    OR it will show a page with list of all matching entries to the query string
    OR throws HTTP 404 error if no match is found
    """
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
            
def show_random(request):
    """Shows a random entry page from available encyclopedia entry"""
    entries = util.list_entries()
    # choose an entry at random
    entry = random.choice(entries)
    return render_entry_page(request, entry)

def add_entry(request):
    """Method to add a new wiki entry page"""
    return render(request, 'encyclopedia/add.html')

def edit_entry(request, entry_name):
    """Method to edit existing wikipedia entry page"""
    entry_content_html = util.get_entry_html(entry_name)
    args = {
            'entry_name': entry_name,
            'entry_content': entry_content_html
            }
    return render(request, 'encyclopedia/add.html', args)

def save_entry(request):
    if request.method == 'POST':
        title = request.POST['title']
        entry_details = request.POST['entry_details']
        entry_details = '# ' + title + '\n\r' + entry_details   # add title on the first line

        # save the new entry content and render the page
        util.save_entry(title, entry_details) 
        return HttpResponseRedirect(reverse('wiki', args = (title,)))

def render_entry_page(request, entry_name):
    entry_content_html = util.get_entry_html(entry_name)
    args = {
            'entry_name': entry_name.title(),
            'entry_content': entry_content_html
            }

    return render(request, 'encyclopedia/wiki.html', args);  


