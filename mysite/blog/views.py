from django.shortcuts import render,get_object_or_404

from .models import Post,comment
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import sessions
blogs=Post.objects.all()  
def starting_page(request):
    return render(request,'home.html',{'allposts':blogs})

def posts(request):
    return render(request,'all-posts.html',{"allposts":blogs})

def post_details(request,slug):
    identified_post = get_object_or_404(Post,slug=slug)
    com=identified_post.comments.all().order_by("-id")
    if request.method == "POST":
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.post = identified_post
            comment.save()
            return HttpResponseRedirect(reverse("post_details",args=[slug]))
    else:
        comment_form = CommentForm()
        return render(request,'post-detail.html',{'singlepost':identified_post,"post_tags":identified_post.tags.all(),"form":comment_form,'comments':com})


