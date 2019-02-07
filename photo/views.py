from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Photo
from django.utils import timezone

def home(request):
    photos = Photo.objects.order_by('-votes_total')
    return render(request, 'photo/home.html', {'photos':photos})

@login_required(login_url="signup")
def create(request):
    if request.method == "POST":
        if request.POST['title'] and request.POST['summary'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            photo = Photo()
            photo.title = request.POST['title']
            photo.summary = request.POST['summary']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                photo.url = request.POST['url']
            else:
                photo.url = 'http://' + request.POST['url']
            photo.icon = request.FILES['icon']
            photo.image = request.FILES['image']
            photo.pub_date = timezone.datetime.now()
            photo.uploader = request.user
            photo.save()
            return redirect('/photo/' + str(photo.id))
        else:
            return render(request, 'photo/create.html', {'error':'Wszystkie pola są wymagane'})
    else:
        return render(request, 'photo/create.html')

def detail(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    return render(request, "photo/detail.html", {'photo':photo})

@login_required(login_url="signup")
def upvote(request, photo_id):
    if request.method == 'POST':
        photo = get_object_or_404(Photo, pk=photo_id)
        photo.votes_total += 1
        photo.save()
        return redirect('/photo/' + str(photo.id))
