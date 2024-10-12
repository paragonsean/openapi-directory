from typing import List, Dict
from aiohttp import web

from openapi_server.models.annotation_layer_get400_response import AnnotationLayerGet400Response
from openapi_server.models.cache_invalidation_request_schema import CacheInvalidationRequestSchema
from openapi_server import util


async def cachekey_invalidate_post(request: web.Request, body) -> web.Response:
    """cachekey_invalidate_post

    Takes a list of datasources, finds the associated cache records and invalidates them and removes the database records

    :param body: A list of datasources uuid or the tuples of database and datasource names
    :type body: dict | bytes

    """
    body = CacheInvalidationRequestSchema.from_dict(body)
    return web.Response(status=200)
