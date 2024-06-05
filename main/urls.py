from django.urls import path

from main.views import AnimeListView, AnimeMediaDetailView, AnimeDetailView, like_anime_media, rate_anime, yana
# from main.views_for_admin import AnimeCreateView, AnimeUpdateView, AnimeMediaUpdateView, AnimeMediaCreateView

urlpatterns = [
    path('', AnimeListView.as_view(), name='anime_list'),
    path('<slug:slug>/', AnimeDetailView.as_view(), name='anime_detail'),
    path('media/<slug:anm_slug>/', AnimeMediaDetailView.as_view(), name='anime_media_detail'),
    path('media/<slug:anm_slug>/like/', like_anime_media, name='like_anime'),
    path('anime/<slug:slug>/rate/', rate_anime, name='rate_anime'),

    # path('create/anime/', AnimeCreateView.as_view(), name='anime_create'),
    # path('create/anime_media', AnimeMediaCreateView.as_view(), name='anime_media_create'),
    # path('update/<slug:slug>/anime', AnimeUpdateView.as_view(), name='anime_update'),
    # path('update/<slug:anm_slug>/anime_media', AnimeMediaUpdateView.as_view(), name='anime_media_update'),
    path('yana/', yana, name='yana'),
]
