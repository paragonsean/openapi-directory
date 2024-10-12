from typing import List, Dict
from aiohttp import web

from openapi_server.models.annotation_layer_get400_response import AnnotationLayerGet400Response
from openapi_server.models.menu_get200_response import MenuGet200Response
from openapi_server import util


async def menu_get(request: web.Request, ) -> web.Response:
    """menu_get

    Get the menu data structure. Returns a forest like structure with the menu the user has access to


    """
    return web.Response(status=200)
