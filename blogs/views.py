from django.shortcuts import render
from django.http import Http404 ,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from .models import post
from .forms import CommentForm


def home_page(request):
    latest_blogs = post.objects.all().order_by("-date")[:4]
    return render(request,"blogs/index.html",{"l_blogs": latest_blogs})


def blogsposts(request):

    blog_details = post.objects.all()
 
    return render (request,"blogs/allposts.html",{"blogs":blog_details})




  
def blog_post(request,blog):
    post_data = post.objects.get(slug=blog)
    tag_caption = post_data.tags.all()
    all_comments = post_data.comments.all().order_by("-id")
     
    if request.method =="POST":
        commented_data = request.POST
        form = CommentForm(commented_data)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post_data
            comment.save()
            return HttpResponseRedirect(reverse("blog-post",args=[blog]))
        return render(request,"blogs/posts.html",{
            "post":post_data,"tags":tag_caption ,"comment_form":form,"comments":all_comments})    
    
    else:
        try:

            form_data = CommentForm()
            return render(request,"blogs/posts.html",{
                "post":post_data,"tags":tag_caption ,"comment_form":form_data,"comments":all_comments})
        except Exception:
            raise Http404()#it is for individual posts












