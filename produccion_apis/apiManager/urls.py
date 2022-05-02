from django.urls import path

from apiManager import views

urlpatterns = [
    path('',views.home,name='HomeFreeToGame'),
    path('games/<str:plataform>/',views.gamesList,name='Games'),
    path('games/<str:plataform>/<str:genre>/',views.gamesList,name='GamesG'),
    path('game/<int:game>/',views.game,name='Game'),
    path('myGames/',views.myGames,name='MyGames'),
    path('search/',views.searchGames,name='SearchGames'),
]