from typing import List, Dict
from aiohttp import web

from openapi_server.models.joke_of_the_day_response import JokeOfTheDayResponse
from openapi_server import util


async def jod_categories_get(request: web.Request, ) -> web.Response:
    """jod_categories_get

    Gets a list of &#x60;Joke of the Day&#x60; Categories. 


    """
    return web.Response(status=200)


async def jod_get(request: web.Request, category=None) -> web.Response:
    """jod_get

    Gets &#x60;Joke of the Day&#x60;. Optional &#x60;category&#x60; param determines the category of returned joke of the day 

    :param category: JOD Category
    :type category: str

    """
    return web.Response(status=200)
