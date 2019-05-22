from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Tournament

import hashlib
import challonge
import random
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

        name = obj.name if len(obj.name) < 8 else (obj.name*2)[:8]

        url = hashlib.md5(name.encode('utf-8')).hexdigest()[:8]
        obj.url = "".join([random.choice(c) for c in url])

        username = "ybourkhanova"
        api_key = "VeiRWinHgxU3W77ZV2q2L70uTI0BnhNnq68iu8Oo"

        challonge.set_credentials(username, api_key)
        tournament = challonge.tournaments.create(obj.name, obj.url) #{"started-at": obj.date})
        tournament_id = tournament["id"]

        obj.id = tournament_id

        obj.save()

        return super().form_valid(form)
