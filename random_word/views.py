from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
# method directing user to home page, where a a random string is displayed with a placeholder, anc counter is @ 0
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    request.session['word'] = get_random_string(length=14)
    return render(request, 'index.html')

# method resets the counter back to zero, when refreshed
def reset(request):
    request.session.flush()
    return redirect('/generate')

