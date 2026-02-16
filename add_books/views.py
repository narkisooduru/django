from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'about.html')
def book_details(request):
    return render(request, 'book_details.html')
def book_list(request):
    return render(request, 'book_list.html')
def contact(request):
    return render(request, 'contact.html')

