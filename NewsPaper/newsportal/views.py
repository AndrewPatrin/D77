from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import PostForm

from django.urls import reverse_lazy


class PostsList(ListView):

    model = Post
    ordering = '-published_date'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class NewsList(PostsList):
    template_name = 'news.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs.filter(type="NW")
class ArticlesList(PostsList):
    template_name = 'articles.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs.filter(type="AR")


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
class NewsDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'post'
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs.filter(type="NW")
class ArticleDetail(DetailView):
    model = Post
    template_name = 'article.html'
    context_object_name = 'post'
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs.filter(type="AR")


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
class NewsCreate(PostCreate):
    template_name = 'news_create.html'
    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'NW'
        return super().form_valid(form)
class ArticleCreate(PostCreate):
    template_name = 'article_create.html'
    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'AR'
        return super().form_valid(form)


class PostSearch(PostsList):
    template_name = 'post_search.html'
class NewsSearch(PostSearch):
    template_name = 'news_search.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs.filter(type="NW")
class ArticleSearch(PostSearch):
    template_name = 'article_search.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs.filter(type="AR")


class PostEdit(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
class NewsEdit(PostEdit):
    template_name = 'news_edit.html'
class ArticleEdit(PostEdit):
    template_name = 'article_edit.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
class NewsDelete(PostDelete):
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')
class ArticleDelete(PostDelete):
    template_name = 'article_delete.html'
    success_url = reverse_lazy('articles_list')