from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Catagory, Post ,Achievement ,Comment
from .forms import CommentForm
# Create your views here.
def home(request):
    return render(request, 'index.html')


class certificateView(ListView):
    model = Achievement
    template_name = 'certificate.html'


def blog(request):
    catagories = Catagory.objects.all()
    post = Post.objects.filter(status=1).order_by("-created_on")[:4]
    context = {"post":post, "catagories":catagories}
    return render(request,'blog.html',context)



#class PostDetail(DetailView):
#     model = Post
#     template_name = 'post_detail.html'


def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)

    catagories = Catagory.objects.all()
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'catagories':catagories
                                           })



def blog_by_catagory(request,pk):
    catagories = Catagory.objects.all()
    catagory_name = list(Catagory.objects.values("name").filter(id=pk)) #find catagory name where id = pk
    post = Post.objects.filter(status=1,catagory_id=pk).order_by("-created_on")
    context = {"post":post, "catagories":catagories ,"catagory_name":catagory_name}
    return render(request,'catagory_page.html',context)
