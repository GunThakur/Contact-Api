from rest_framework import filters
import django_filters
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import render
from django.views import generic
from rest_framework import generics
from .models import Post, contact
from rest_framework import viewsets
from .serializers import contactserializer
import requests
from .forms import SearchForm

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.all().filter(status=True).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


def save_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        country = request.POST.get('country', '')
        problem = request.POST.get('problem', '')
        data = contact(name=name, email=email,
                       country=country, problem=problem)
        data.save()
    return render(request, 'contact_us.html')


def about_us(request):
    return render(request, 'about_us.html')


def policy(request):
    return render(request, 'policy.html')


class contactviewset(viewsets.ModelViewSet):
    queryset = contact.objects.all()
    serializer_class = contactserializer


class search(generics.ListAPIView):
    queryset = contact.objects.all()
    serializer_class = contactserializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
