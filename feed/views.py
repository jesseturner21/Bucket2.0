from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from profiles.models import Content, Like

@login_required
def feed(request):
    user = request.user
    content = Content.objects.all()
    return render(request, 'feed.html', {'user': user, 'content':content})

@login_required
def like_content(request, content_id):
    content = get_object_or_404(Content, id=content_id)
    like, created = Like.objects.get_or_create(user=request.user, content=content)

    if not created:
        # The like already exists, so we remove it.
        like.delete()
        return redirect('feed')
    else:
        # The like is newly created.
        return redirect('feed')