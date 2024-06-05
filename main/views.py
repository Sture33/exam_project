from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, TemplateView, DetailView

from anime_app.models import Anime, AnimeMedia, Comments, Rating
from main.forms import CommentForm


class AnimeListView(ListView):
    model = Anime
    template_name = 'main/temps/main.html'


class AnimeDetailView(TemplateView):
    template_name = 'main/temps/anime_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        anime_slug = self.kwargs.get('slug')
        anime = Anime.objects.get(slug=anime_slug)

        context['anime'] = anime
        context['anime_medias'] = AnimeMedia.objects.filter(anime=anime)
        context['average_rating'] = anime.get_average_rating()
        return context


class AnimeMediaDetailView(DetailView):
    model = AnimeMedia
    template_name = 'main/temps/anime_media_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'anm_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        anime_media = get_object_or_404(AnimeMedia, slug=self.kwargs['anm_slug'])
        context['comments'] = Comments.objects.filter(anime_media=anime_media)
        context['form'] = CommentForm()
        context['total_likes'] = anime_media.get_total_likes()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.anime_media = self.object
            comment.user = request.user
            comment.save()
            return redirect('anime_media_detail', anm_slug=self.object.slug)
        return redirect('anime_media_detail', anm_slug=self.object.slug)


def like_anime_media(request, anm_slug):
    anime_media = get_object_or_404(AnimeMedia, slug=anm_slug)
    if request.user in anime_media.likes.all():
        anime_media.likes.remove(request.user)
    else:
        anime_media.likes.add(request.user)
    return redirect('anime_media_detail', anm_slug=anm_slug)


def rate_anime(request, slug):
    anime = get_object_or_404(Anime, slug=slug)
    if request.method == 'POST':
        rating_value = int(request.POST.get('rating'))
        rating, created = Rating.objects.get_or_create(user=request.user, anime=anime)
        anime.user_is_rating = True
        rating.value = rating_value
        anime.save()
        rating.save()
        return redirect('anime_detail', slug=slug)


def yana(request):
    return render(request, 'main/you_are_not_admin.html')
