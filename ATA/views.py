from django.shortcuts import render
from .models import Mentor, Mentee, Blog
from .forms import inputmentor, inputmentee, inputblog 
from django.shortcuts import redirect

# Create your views here.
def Home(request):
    return render(request, 'home.html', {})

def Blogs(request):
    blog_ = Blog.objects.all()
    return render(request, 'blog.html', {'blog': blog_})

def Mentees(request):
    mentee_ = Mentee.objects.all()
    return render(request, 'mentee.html', {'mentee': mentee_})

def Mentors(request):
    mentor_ = Mentor.objects.all()
    return render(request, 'mentor.html', {'mentor': mentor_})

def Author(request):
    return render(request, 'author.html', {})

def listmentor(request):
    if request.method == 'POST':
        form = inputmentor(request.POST)
        if form.is_valid():
            post =form.save(commit=False)
            post.save()
            return redirect ('Halaman_Mentor')
    else:
        form = inputmentor()
    return render(request, 'input_mentor.html',{'form':form})

def listmentee(request):
    if request.method == 'POST':
        form = inputmentee(request.POST)
        if form.is_valid():
            post =form.save(commit=False)
            post.save()
            return redirect ('Halaman_Mentee')
    else:
        form = inputmentee()
    return render(request, 'input_mentee.html',{'form':form})

def listblog(request):
    if request.method == 'POST':
        form = inputblog(request.POST)
        if form.is_valid():
            post =form.save(commit=False)
            post.save()
            return redirect ('Halaman_Blog')
    else:
        form = inputblog()
    return render(request, 'input_blog.html',{'form':form})