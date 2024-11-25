
from django.shortcuts import render
from django.http import JsonResponse

def hello_world(request):
    # Check query parameter to switch between JSON and HTML
    if request.GET.get('format') == 'html':
        return render(request, 'hello/hello.html')  # Render the HTML template
    return JsonResponse({"Message": "Hello World!"})  # Default to JSON
