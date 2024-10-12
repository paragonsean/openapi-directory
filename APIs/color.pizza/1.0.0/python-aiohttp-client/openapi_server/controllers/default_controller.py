from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.get200_response import Get200Response
from openapi_server.models.lists_get200_response import ListsGet200Response
from openapi_server.models.possible_lists import PossibleLists
from openapi_server import util


async def lists_get(request: web.Request, ) -> web.Response:
    """Get all colors of the default color name list

    


    """
    return web.Response(status=200)


async def names_get(request: web.Request, name, list=None) -> web.Response:
    """Get all colors of the default color name list

    

    :param name: The name of the color to retrieve (min 3 characters)
    :type name: str
    :param list: The name of the color name list to use
    :type list: dict | bytes

    """
    list = .from_dict(list)
    return web.Response(status=200)


async def root_get(request: web.Request, list=None, values=None, noduplicates=None) -> web.Response:
    """Get all colors of the default color name list

    

    :param list: The name of the color name list to use
    :type list: dict | bytes
    :param values: The hex values of the colors to retrieve without &#39;#&#39;
    :type values: str
    :param noduplicates: Allow duplicate names or not
    :type noduplicates: bool

    """
    list = .from_dict(list)
    return web.Response(status=200)


async def swatch_get(request: web.Request, color, name=None) -> web.Response:
    """Generate a color swatch for any color

    

    :param color: The hex value of the color to retrieve without &#39;#&#39;
    :type color: str
    :param name: The name of the color
    :type name: str

    """
    return web.Response(status=200)
