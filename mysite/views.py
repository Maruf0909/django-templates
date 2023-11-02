from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse


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
        return render(request, 'blogs.html')