from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def cast_info_detailed_info(request: web.Request, id) -> web.Response:
    """cast_info_detailed_info

    

    :param id: Movie ID. You can use the movies search endpoint or peruse the lists of movies/dvds to get the Movie ID
    :type id: str

    """
    return web.Response(status=200)


async def movie_clips_detailed_info(request: web.Request, id) -> web.Response:
    """movie_clips_detailed_info

    

    :param id: Movie ID. You can use the movies search endpoint or peruse the lists of movies/dvds to get the Movie ID
    :type id: str

    """
    return web.Response(status=200)


async def movies_alias_detailed_info(request: web.Request, id=None, type=None) -> web.Response:
    """movies_alias_detailed_info

    

    :param id: Movie ID. You can use the movies search endpoint or peruse the lists of movies/dvds to get the Movie ID
    :type id: str
    :param type: Only supports imdb lookup at this time
    :type type: str

    """
    return web.Response(status=200)


async def movies_info_detailed_info(request: web.Request, id) -> web.Response:
    """movies_info_detailed_info

    

    :param id: Movie ID. You can use the movies search endpoint or peruse the lists of movies/dvds to get the Movie ID
    :type id: str

    """
    return web.Response(status=200)


async def movies_reviews_detailed_info(request: web.Request, id, review_type=None, page_limit=None, page=None, country=None) -> web.Response:
    """movies_reviews_detailed_info

    

    :param id: Movie ID. You can use the movies search endpoint or peruse the lists of movies/dvds to get the Movie ID
    :type id: str
    :param review_type: 3 different review types are possible: &#39;all&#39;, &#39;top_critic&#39; and &#39;dvd&#39;. &#39;top_critic&#39; shows all the Rotten Tomatoes designated top critics. &#39;dvd&#39; pulls the reviews given on the DVD of the movie. &#39;all&#39; as the name implies retrieves all reviews.
    :type review_type: str
    :param page_limit: The number of reviews to show per page
    :type page_limit: str
    :param page: The selected page of reviews
    :type page: str
    :param country: Provides localized data for the selected country (ISO 3166-1 alpha-2) if available. Otherwise, returns US data.
    :type country: str

    """
    return web.Response(status=200)


async def movies_similar_detailed_info(request: web.Request, id, limit=None) -> web.Response:
    """movies_similar_detailed_info

    

    :param id: Movie ID. You can use the movies search endpoint or peruse the lists of movies/dvds to get the Movie ID
    :type id: str
    :param limit: Limit the number of similar movies to show
    :type limit: str

    """
    return web.Response(status=200)
