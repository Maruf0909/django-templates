from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse
from .models import Blog


class HomeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'home.html')


class AboutView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'about.html')


class ContactView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'contact.html')


class BlogsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        content = {
            'blogs': [{'id': blog.id, 'title': blog.title, 'content': blog.content[:100], 'published': blog.published} for blog in Blog.objects.all()]
        }
        return render(request, 'blogs.html', context=content)