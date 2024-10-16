from django.shortcuts import render
from django.views.generic import ListView, DetailView
from album.models import Team, Player

# Create your views here.
class TeamListView(ListView):
    model = Team


# Vista de jugadores
class PlayerListView(ListView):
    model = Player

# Vista detalle equipo
class TeamDetailView(DetailView):
    model = Team

# Vista detalle jugador
class PlayerDetailView(DetailView):
    model = Player