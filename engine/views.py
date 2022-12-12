from django.shortcuts import render, HttpResponse, redirect
from .forms import AddNews


def allNews(request):
    posts = []

    title = request.POST.get('title')
    content = request.POST.get('content')
    isPublish = request.POST.get('isPublish')
    date = request.POST.get('date')

    newPost = {
        'title': title,
        'content': content,
        'isPublish': isPublish,
        'date': date
    }

    posts.append(newPost)
    return render(request, 'engine/allNews.html', context={'posts': posts})


def addNews(request):
    if request.method == 'POST':
        return redirect(allNews)
    else:
        form = AddNews()
        return render(request, 'engine/addNews.html', context={'form': form})
