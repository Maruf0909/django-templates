from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse



class HomeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'home.html')