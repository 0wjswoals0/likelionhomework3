from django.shortcuts import redirect, render, get_object_or_404
from .models import Blog
#redirect, render로 수정됨 원본:render

# Create your views here.
#def home(request):
    #blogs = Blog.objects.all()
    #return render(request, 'home.html',{'blogs':blogs})
def detail(request,blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'detail.html', {'blog':blog})

def create(request):
    if request.method=='POST':
        new_blog = Blog()

        new_blog.title = request.POST['title']
        new_blog.content = request.POST['content']

        new_blog.save()

        return redirect('detail', new_blog.id)
    return render(request, 'new.html')

def home(request):
    blog = Blog.objects.all()
    return render(request, 'home.html', {'blogs':blog})