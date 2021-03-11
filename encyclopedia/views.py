from django.shortcuts import render
from markdown2 import Markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def convert_to_html(entry):
    markdown = Markdown()
    entry_page = util.get_entry(entry)
    converted_entry = markdown.convert(entry_page) if entry_page else None
    return converted_entry

def entry(request, entry):
    converted_entry = convert_to_html(entry)
    if converted_entry is None:
        return render(request, "encyclopedia/entry_doesnt_exist.html", {
            "entry_title": entry.upper()
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": converted_entry,
            "entry_title": entry.upper()
        })

def new(request):
    return render(request, "encyclopedia/new.html")

def save(request):
    if request.method == 'POST':
        input_title = request.POST['title']
        input_text = request.POST['text']
        entries = util.list_entries()
        if input_title in entries:
            return render(request, 'encyclopedia/entry_exists')
        else:
            util.save_entry(input_title, input_text)
            converted_entry = convert_to_html(input_title)
            return render(request, "encyclopedia/entry.html", {
                "entry": converted_entry,
                "entry_title": input_title
            })