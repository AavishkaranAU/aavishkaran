from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def past_events(request):
    return render(request,'past_events.html')
