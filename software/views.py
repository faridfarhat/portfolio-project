from django.shortcuts import render

# Create your views here.
def software(request):
    return render(request, 'software/software.html')