from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_movies,get_movie,search_movie


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting news articles
    tesla_news = get_news_article('tesla')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    title = 'Home - Welcome to The best News resource Online'
    return render_template('index.html', title = title, tesla = _movies, upcoming = upcoming_movie, now_showing = now_showing_movie )

@app.route('/movie/<int:id>')
def movie(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_movie(id)
    title = f'{movie.title}'

    return render_template('movie.html',title = title,movie = movie)