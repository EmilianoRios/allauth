from django.shortcuts import redirect, render, HttpResponse
import requests

# Create your views here.

''' NAVBAR - MENU
* HOME 
* GAMES LIST
* MY GAMES
* SEARCH GAMES'''


# * HOME
def home(request):

    url = request.path

    return render(request,'apiManager/home.html',{'url':url})

# * GAMESLIST
def gamesList(request,plataform='None',genre=None):

    if 'all' in request.path:
        plataformGenre = 'all'
    elif 'pc' in request.path:
        plataformGenre = 'pc'
    elif 'browser' in request.path:
        plataformGenre = 'browser'

    sortBy = request.GET.get('sort_by')

    if plataform == 'all' and genre==None and sortBy==None:
        URL = 'https://www.freetogame.com/api/games' #configuramos la url
    elif plataform == 'pc' and genre==None and sortBy==None:
        URL = 'https://www.freetogame.com/api/games?platform=pc' #configuramos la url
    elif plataform == 'browser' and genre==None and sortBy==None:
        URL = 'https://www.freetogame.com/api/games?platform=browser' #configuramos la url
    elif plataform == 'all' and genre and sortBy==None:
        URL = 'https://www.freetogame.com/api/games?platform=%s&category=%s&sort-by=relevance'%(plataform,genre)#configuramos la url
    elif plataform == 'pc' and genre and sortBy==None:
        URL = 'https://www.freetogame.com/api/games?platform=%s&category=%s&sort-by=relevance'%(plataform,genre)#configuramos la url
    elif plataform == 'browser' and genre and sortBy==None:
        URL = 'https://www.freetogame.com/api/games?platform=%s&category=%s&sort-by=relevance'%(plataform,genre)#configuramos la url
    elif plataform == 'all' and genre and sortBy:
        URL = 'https://www.freetogame.com/api/games?platform=all&category=%s&sort-by=%s'%(genre,sortBy)#configuramos la url
    elif plataform == 'pc' and genre and sortBy:
        URL = 'https://www.freetogame.com/api/games?platform=%s&category=%s&sort-by=%s'%(plataform,genre,sortBy)#configuramos la url
    elif plataform == 'browser' and genre and sortBy:
        URL = 'https://www.freetogame.com/api/games?platform=%s&category=%s&sort-by=%s'%(plataform,genre,sortBy)#configuramos la url
    elif plataform == 'all' and genre==None and sortBy:
        URL = 'https://www.freetogame.com/api/games?sort-by=%s&platform=%s'%(sortBy,plataform)#configuramos la url
    elif plataform == 'pc' and genre==None and sortBy:
        URL = 'https://www.freetogame.com/api/games?sort-by=%s&platform=%s'%(sortBy,plataform)#configuramos la url
    elif plataform == 'browser' and genre==None and sortBy:
        URL = 'https://www.freetogame.com/api/games?sort-by=%s&platform=%s'%(sortBy,plataform)#configuramos la url
        
    dataGames = requests.get(URL) #solicitamos la información y guardamos la respuesta en data.

    dataGames = dataGames.json() #convertimos la respuesta en dict

    return render(request,'apiManager/gamesList.html',{'games':dataGames,'plataformGenre':plataformGenre})

# * MYGAMES
def myGames(request):
    return render(request,'apiManager/myGames.html')

# * SEARCHGAMES
def searchGames(request):

    succesGames = []

    if request.method == 'POST':
        search = request.POST.get('Search').lower()

        URL = 'https://www.freetogame.com/api/games' #configuramos la url

        dataGames = requests.get(URL) #solicitamos la información y guardamos la respuesta en data.

        dataGames = dataGames.json() #convertimos la respuesta en dict

        for game in dataGames:
            if search in game['title'].lower():
                succesGames.append(game)

    return render(request,'apiManager/searchGames.html',{'games':succesGames})

# ? GAME
def game(request,game):

    URL = 'https://www.freetogame.com/api/game?id=' + str(game) #configuramos la url

    dataGame = requests.get(URL) #solicitamos la información y guardamos la respuesta en data.

    dataGame = dataGame.json() #convertimos la respuesta en dict

    return render(request,'apiManager/game.html',{'game':dataGame})