from django.shortcuts import render
from django.views import generic
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


def display_data(request):
    api_url = 'http://localhost:7000/blogweb/contact/'
    response = requests.get(api_url).json()
    return render(request, 'search.html', {'response': response})


# def search(request):
#     api_url = 'http://localhost:7000/blogweb/contact/'
#     form = SearchForm(request.GET)
#     queryset = requests.get(api_url).json()
#     if form.is_valid():
#         search_query = form.cleaned_data['search_query']
#         queryset = queryset.filter(name__icontains=search_query)
#     context = {
#         'form': form,
#         'results': queryset,
#     }
#     return render(request, 'search.html', context)
