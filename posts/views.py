from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post
# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'posts_list.html'

    def get_queryset(self):
        return self.model.objects.order_by('-date')


class PostDetailView(DeleteView):
    model = Post
    template_name = 'post_detail.html'


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body', 'document']
    template_name = 'post_edit.html'

    def form_valid(self, form):
        #doc = self.request.body.decode('utf-8').split("&")[-1].split('=')[-1]

        obj = form.save(commit=False)
        #obj.document = doc
        obj.save()

        return super().form_valid(form)


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts_list')


class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body', 'document']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()

        return super().form_valid(form)
