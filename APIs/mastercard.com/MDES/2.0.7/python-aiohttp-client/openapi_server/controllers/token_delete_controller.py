from typing import List, Dict
from aiohttp import web

from openapi_server.models.errors_response import ErrorsResponse
from openapi_server.models.token_delete_request_schema import TokenDeleteRequestSchema
from openapi_server.models.token_delete_response_schema import TokenDeleteResponseSchema
from openapi_server import util


async def token_delete_post(request: web.Request, token_delete_request_schema=None) -> web.Response:
    """token_delete_post

    Used to delete a token so that it may not initiate any new transactions. All authorizations for a deleted token will be declined. A deleted token may not be returned to an active state. 

    :param token_delete_request_schema: Contains the details of the request message.
    :type token_delete_request_schema: dict | bytes

    """
    token_delete_request_schema = TokenDeleteRequestSchema.from_dict(token_delete_request_schema)
    return web.Response(status=200)
