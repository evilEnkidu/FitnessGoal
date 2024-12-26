from django.shortcuts import render

# Create your views here.
def home_page(request):
      return render(request, 'pages/home.html')

def about_page(request):
      return render(request, 'pages/about.html')