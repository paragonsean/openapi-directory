from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def g_et_swagger_doc_format(request: web.Request, ) -> web.Response:
    """Swagger compatible API description

    


    """
    return web.Response(status=200)


async def g_et_swagger_doc_name_format(request: web.Request, name) -> web.Response:
    """Swagger compatible API description for specific API

    

    :param name: Resource name of mounted API
    :type name: str

    """
    return web.Response(status=200)
