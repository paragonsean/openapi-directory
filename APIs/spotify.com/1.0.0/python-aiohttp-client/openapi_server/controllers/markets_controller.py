from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_available_markets200_response import GetAvailableMarkets200Response
from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server import util


async def get_available_markets(request: web.Request, ) -> web.Response:
    """Get Available Markets 

    Get the list of markets where Spotify is available. 


    """
    return web.Response(status=200)
