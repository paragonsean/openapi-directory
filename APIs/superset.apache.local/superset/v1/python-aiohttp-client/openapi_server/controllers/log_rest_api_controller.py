from typing import List, Dict
from aiohttp import web

from openapi_server.models.annotation_layer_get400_response import AnnotationLayerGet400Response
from openapi_server.models.get_item_schema import GetItemSchema
from openapi_server.models.get_list_schema import GetListSchema
from openapi_server.models.log_get200_response import LogGet200Response
from openapi_server.models.log_pk_get200_response import LogPkGet200Response
from openapi_server.models.log_post201_response import LogPost201Response
from openapi_server.models.log_rest_api_post import LogRestApiPost
from openapi_server import util


async def log_get(request: web.Request, q=None) -> web.Response:
    """log_get

    Get a list of models

    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def log_pk_get(request: web.Request, pk, q=None) -> web.Response:
    """log_pk_get

    Get an item model

    :param pk: 
    :type pk: int
    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def log_post(request: web.Request, body) -> web.Response:
    """log_post

    

    :param body: Model schema
    :type body: dict | bytes

    """
    body = LogRestApiPost.from_dict(body)
    return web.Response(status=200)
