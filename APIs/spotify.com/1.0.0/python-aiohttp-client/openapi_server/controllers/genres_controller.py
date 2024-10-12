from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server.models.get_recommendation_genres200_response import GetRecommendationGenres200Response
from openapi_server import util


async def get_recommendation_genres(request: web.Request, ) -> web.Response:
    """Get Available Genre Seeds 

    Retrieve a list of available genres seed parameter values for [recommendations](/documentation/web-api/reference/get-recommendations). 


    """
    return web.Response(status=200)
