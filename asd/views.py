from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Album
from .forms import registrarAlbumForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class mostrar(ListView):
    model = Album
    template_name = "asd/listaralbumes.html"
    ordering = ['artista']

class agregar(LoginRequiredMixin, CreateView):
    model = Album
    form_class = registrarAlbumForm
    template_name = "asd/agregaralbum.html"
    success_url = reverse_lazy('album_Listar')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class actualizar(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Album
    form_class = registrarAlbumForm
    template_name = "asd/agregaralbum.html"
    success_url = reverse_lazy('album_Listar')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == Album.autor:
            return True
        return False

class eliminar(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Album
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == Album.autor:
            return True
        return False

class detallar(DetailView):
    model = Album
    template_name = "asd/detallaralbum.html"
