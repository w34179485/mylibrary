from django.shortcuts import render,get_object_or_404
from .models import Library,Book,Author,Reader,Record

def index(request):
    library = Library.objects.first()
    context = {'library':library}
    context['authors'] = Author.objects.all()
    return render(request,'library/index.html',context)

def author(request,author_id):
    author = get_object_or_404(Author,pk=author_id)
    return render(request,'library/author.html',{'author':author})
