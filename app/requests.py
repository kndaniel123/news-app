import urllib.request,json
from .models import News


News = News

# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_news(q):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(q,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None  #replacable with []

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_articles(news_results_list)


    return news_results

def process_articles(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
   
    news_results = []
    for news_item in news_list:
       
        title = news_item.get('title')
        author = news_item.get('author')
        description = news_item.get('description')
        url = news_item.get('url')
        poster = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')

        if poster:
            news_object = News(title,author,description,url,poster,publishedAt,content)
            news_results.append(news_object)

    return news_results

'''
def get_movie(id):
    get_movie_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None  #replacable with []
        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')

            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)

    return movie_object    

'''
