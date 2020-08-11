from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import markdown2
from . import util
import re
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import random
items=[]




def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })




def detail(request,title):

    #return HttpResponse(file)
    file =markdown2.markdown(util.get_entry(title))

    return render(request,'encyclopedia/details.html',{
    "filename":file,"title":title,
    })

def add(request):

    if request.method =="POST":
        title=request.POST.get('title',False)
        content = request.POST.get('body',False)
        check_title =  f"entries/{title}.md"
        if default_storage.exists(check_title):
            message = "this name already exists"
            return render(request,"encyclopedia/search_result.html",{"title":title,"message":message})
        util.save_entry(title, content)
        file =markdown2.markdown(util.get_entry(title))
        return render(request,'encyclopedia/details.html',{"filename":file,'title':title})
    return render(request,"encyclopedia/add.html")



def search(request):
    #if request.method=="POST":
    key = request.POST.get('query',False)
    filename = f"entries/{key}.md"
    if default_storage.exists(filename):
        file =markdown2.markdown(util.get_entry(key))

        return render(request,'encyclopedia/details.html',{
        "filename":file,'title':key
        })
    else:
        _, filenames = default_storage.listdir("entries")
        files =list(sorted(re.sub(r"\.md$", "", filename)
                    for filename in filenames if filename.endswith(".md")))
        items=[]
        for item in files:
            if key.lower() in item.lower():
                items.append(item)
        return render(request,"encyclopedia/search_result.html",{"items":items})




def edit(request,title):
    #return HttpResponse(file)
    file =util.get_entry(title)

    return render(request,'encyclopedia/edit.html',{
    "file":file,"title":title
    })


def save_edit(request,title):
        content = request.POST.get('body',False)
        util.save_entry(title, content)
        file =markdown2.markdown(util.get_entry(title))
        return render(request,'encyclopedia/details.html',{"filename":file,"title":title})





    #return HttpResponseRedirect(reverse("index"))

def random_call(request):
    _, filenames = default_storage.listdir("entries")
    files =list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))
    title = random.choice(files)


    file =markdown2.markdown(util.get_entry(title))

    return render(request,'encyclopedia/details.html',{
    "filename":file,"title":title,
        })
