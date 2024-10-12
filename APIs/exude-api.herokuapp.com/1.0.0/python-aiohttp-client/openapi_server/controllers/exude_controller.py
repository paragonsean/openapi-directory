from typing import List, Dict
from aiohttp import web

from openapi_server.models.exude_response_bean import ExudeResponseBean
from openapi_server import util


async def filter_file_data_stoppings(request: web.Request, type, file=None) -> web.Response:
    """Filter the stopping words from the provided input file

    

    :param type: provide the type of filtering required stopping/swear
    :type type: str
    :param file: 
    :type file: str

    """
    return web.Response(status=200)


async def filter_stoppings(request: web.Request, type, data=None, links=None) -> web.Response:
    """Filter the stopping words from the provided input data or links

    

    :param type: provide the type of filtering required stopping/swear
    :type type: str
    :param data: 
    :type data: str
    :param links: 
    :type links: List[str]

    """
    return web.Response(status=200)
