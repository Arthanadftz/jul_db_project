from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Tournament
# Create your views here.


class TournamentListView(ListView):
    model = Tournament
    template_name = 'tournaments_list.html'

    def get_queryset(self):
        return self.model.objects.order_by('-date')


class TournamentDetailView(DetailView):
    model = Tournament
    template_name = 'tournament_detail.html'


class TournamentCreateView(CreateView):
    model = Tournament
    template_name = 'tournament_new.html'
    fields = ['name']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()

        return super().form_valid(form)

"""class TournamentUpdateView(UpdateView):
    model = Tournament
    fields = ['title', 'body', 'document']
    template_name = 'tournament_edit.html'

    def form_valid(self, form):
        #doc = self.request.body.decode('utf-8').split("&")[-1].split('=')[-1]

        obj = form.save(commit=False)
        #obj.document = doc
        obj.save()

        return super().form_valid(form)"""


"""class TournamentDeleteView(DeleteView):
    model = Tournament
    template_name = 'tournament_delete.html'
    success_url = reverse_lazy('tournaments_list')
"""
