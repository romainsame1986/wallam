from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'


class WorkPageView(TemplateView):
    template_name = 'how_works.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'


class AnnoncePageView(TemplateView):
    template_name = 'annonce.html'
