from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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

# Vista agregar equipo
class TeamCreate(CreateView):
    model = Team
    fields = '__all__'

# Vista agregar jugador
class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'

# Vista modificar equipo
class TeamUpdate(UpdateView):
    model = Team
    fields = '__all__'

# Vista modificar jugador
class PlayerUpdate(UpdateView):
    model = Player
    fields = '__all__'

# Vista eliminar equipo
class TeamDelete(DeleteView):
    model = Team
    success_url = reverse_lazy('team-list')

# Vista eliminar jugador
class PlayerDelete(DeleteView):
    model = Player
    success_url = reverse_lazy('player-list')