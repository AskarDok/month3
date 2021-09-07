
from django.shortcuts import render, redirect

# Create your views here.
from datetime import datetime
from django.conf import settings
from django.http import HttpResponse, FileResponse, HttpResponseRedirect
import random
from .models import *
from django.views import generic
from .forms import *
from rest_framework.generics import ListAPIView


class BlogView(generic.ListView):
    template_name = 'index.html'
    queryset = Blog.objects.all()
    context_object_name = 'posts'




class BlogDetailView(generic.DetailView, generic.CreateView):
    form_class = CreateComment
    template_name = 'detail.html'
    queryset = Blog.objects.all()
    context_object_name = 'post'
    extra_context = {"comments": Comment.objects.all()}

    def get_context_data(self, *args, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        blog_id = self.kwargs['pk']
        commenta = Comment.objects.filter(blog_id=blog_id)
        context['comments'] = commenta
        return context



    def post(self, request, **kwargs):
        if request.method == "POST":
            form = self.request.POST
            comment = form['comments']
            Comment.objects.create(text=comment, blog_id=self.kwargs['pk'])
            return HttpResponseRedirect('/blog/')




def date_view(request):
    today = datetime.now()
    return HttpResponse(str(today))


def view_random(request):
    num = random.randint(1, 100)
    data = {'num': num,
            'title': 'random numbers'}
    return render(request, 'random.html', context=data)


def image_view(request):
    path = settings.BASE_DIR / 'static' / '123.jpg'
    file = open(path, 'rb')
    return FileResponse(file)


def view_students(request):
    students = Student.objects.all()
    data = {'students': students,
            'title': 'students',
            }
    return render(request, 'students.html', context=data)


def create_post(request):
    if request.method == "POST":
        form = request.POST
        title = form['title']
        description = form['description']
        hashtags = form['hashtags']
        image = request.FILES['image']
        Blog.objects.create(title=title, description=description, hashtags=hashtags, image=image)
        return redirect('/blog/')
    if request.method == "GET":
        return render(request, 'create.html')

class BlogListApiView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer