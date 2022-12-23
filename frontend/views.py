from django.shortcuts import render


# Create your views here.
def index(request):
  return render(request, 'index.html')


def about(request):
  return render(request, 'AboutUsPage.html')

def contact(request):
  return render(request, 'ContactPage.html')