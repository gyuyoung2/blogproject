from .forms import CreatePostForm
from django.shortcuts import get_object_or_404, redirect, render
from .models import Page
from django.utils import timezone

# Create your views here.

def home(request):
    pages = Page.objects
    return render(request,'home.html', {'pages' : pages})

def detail(request, page_id):
    page_detail = get_object_or_404(Page, pk = page_id)
    return render(request, 'detail.html', {'page_detail' : page_detail})

def create(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.pub_date = timezone.datetime.now()
            page.save()
        return redirect('/detail/' + str(page.id))
    else:
        form = CreatePostForm()
    return render(request, 'create.html', {'form' : form})

def update(request, page_id):
    page = Page.objects.get(id=page_id)
    if request.method == "POST":
        form = CreatePostForm(request.POST, instance = page)
        if form.is_valid():
            page = form.save()
            return redirect('/detail/'+str(page.id))
    else:
        form = CreatePostForm(instance = page)
        return render(request, 'create.html', {'form':form})

def delete(request, page_id):
    page = Page.objects.get(id=page_id)
    page.delete()
    return redirect('home')



    

