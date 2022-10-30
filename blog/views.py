from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


posts=[
      {
      'author':'Kris',
      'title':'blog post 1',
      'content':' This is the post',
      'date_posted':'August 27, 2022',
            },
       {
      'author':'Zed',
      'title':'blog post 2',
      'content':'Another Post from him',
      'date_posted':'September 27, 2022',
            }
      ]


def home(request):
      
      context={
            'posts':posts
            }
      return render(request,'blog/home.html',context)

def about(request):
      return render(request,'blog/about.html')


def tfcount(request):
      return render(request,'blog/tfcount.html')
