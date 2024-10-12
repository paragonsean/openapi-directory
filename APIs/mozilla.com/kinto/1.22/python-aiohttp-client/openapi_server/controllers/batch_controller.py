from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_payload_schema import BatchPayloadSchema
from openapi_server.models.batch_response_body_schema import BatchResponseBodySchema
from openapi_server.models.error_schema import ErrorSchema
from openapi_server import util


async def batch(request: web.Request, body) -> web.Response:
    """batch

    

    :param body: 
    :type body: dict | bytes

    """
    body = BatchPayloadSchema.from_dict(body)
    return web.Response(status=200)
