
from django.shortcuts import render, redirect, get_object_or_404
from .forms import URLForm
from .models import URL

def home(request):
    form = URLForm()
    short_url = None

    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url_obj = form.save()
            short_url = request.build_absolute_uri(f"/{url_obj.shortcode}")

    return render(request, 'shortener/home.html', {'form': form, 'short_url': short_url})

def redirect_url(request, shortcode):
    url_obj = get_object_or_404(URL, shortcode=shortcode)
    return redirect(url_obj.original_url)


# Create your views here.
