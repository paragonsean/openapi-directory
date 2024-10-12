from typing import List, Dict
from aiohttp import web

from openapi_server.models.basic_error import BasicError
from openapi_server.models.code_of_conduct import CodeOfConduct
from openapi_server import util


async def codes_of_conduct_get_all_codes_of_conduct(request: web.Request, ) -> web.Response:
    """Get all codes of conduct

    


    """
    return web.Response(status=200)


async def codes_of_conduct_get_conduct_code(request: web.Request, key) -> web.Response:
    """Get a code of conduct

    

    :param key: 
    :type key: str

    """
    return web.Response(status=200)
