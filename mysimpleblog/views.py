from django.shortcuts import redirect, render , get_object_or_404
from django.views.generic import ListView, DetailView, CreateView , UpdateView , DeleteView
from .models import Post , Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy , reverse
from django.http import HttpResponseRedirect

# ListView : it is a query set which will do a query to get all the list of records and bring them on webpage
# detailView: It a query set which bring the data of one record i.e., details of one record on webpage


# def home(request):
#     return render(request, 'home.html', {})

# Here we are creating the "Class" based views rather than the "function based"

class HomeView(ListView):
    model = Post  # Post is coming from the model.py
    template_name = 'home.html'
    # ordering = ['-id']  #from last added to first
    # ordering = ['id']
    ordering = ['-post_date']

    # Writing a fucntion to get the categories on home navbar
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context





class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    # fields = ('title', 'body')
    # fields = '__all__'
    form_class = PostForm

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    # fields = '__all__'
    # fields = ['title', 'title_tag', 'body']
    form_class = EditForm

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    # fields = ('title', 'body')
    fields = '__all__'
    # form_class = PostForm


# Using fuction based view for the category name pages

def CategoryView(request, cats):
    # category_posts = Post.objects.filter(category = cats)
    category_posts = Post.objects.filter(category = cats.replace('-', ' ')) #Here we are replacing the space with '-' in url which is called slugify. the slugify added in home.html at category url link.
    return render(request, 'categories.html', {'cats' : cats.title().replace('-',' '), 'category_posts' : category_posts}) # here title is used to make first letter caps and replaced used to sluify the url link
    # return render(request, 'categories.html', {'cats' : cats.title(), 'category_posts' : category_posts}) # here title is used to make first letter caps and replaced used to sluify the url link


# Creating a separate categories page itself.

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list' : cat_menu_list })


def LikeView(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user) 
        liked = True

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))



class AddCommentView(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    # fields = '__all__'
    form_class = CommentForm
    

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    success_url = reverse_lazy('home')