from typing import List, Dict
from aiohttp import web

from openapi_server.models.movie import Movie
from openapi_server import util


async def get_movies(request: web.Request, ) -> web.Response:
    """Get the status of your movies

    Get the status any of your movies by passing your project ID in the &lt;code&gt;project&lt;/code&gt; query parameter. You can get your project ID from the response of the POST request.


    """
    return web.Response(status=200)


async def new_movie(request: web.Request, body) -> web.Response:
    """Create a new movie

    Submit a new movie rendering job.

    :param body: 
    :type body: dict | bytes

    """
    body = Movie.from_dict(body)
    return web.Response(status=200)
