import re
import markdown2

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries(lower=False):
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    entries = list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))   # return sorted list of filenames ending with .md by removing its extension

    if lower:
        return [e.lower() for e in entries]
    else:
        return entries

def list_matching_entries(query: str):
    """
    Returns a list of all names of encyclopedia entries matching the query string.
    """
    _, filenames = default_storage.listdir("entries")
    entries = list(sorted(re.sub(r"\.md$", "", filename) for filename in filenames 
                            if filename.endswith(".md") and 
                            query.lower() in filename.lower()))   # return sorted list of filenames ending with .md by removing its extension

    return entries


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

def get_entry_html(entry):
    """
    Retrieves an encyclopedia entry by its title and converts it into HTML string. 
    If no such entry exists, the function returns None.
    """
    entry_content = get_entry(entry.title())

    if entry_content:
        entry_content = markdown2.markdown(entry_content)
    
    return entry_content