from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_exception import BadRequestException
from openapi_server.models.put_events_request import PutEventsRequest
from openapi_server import util


async def put_events(request: web.Request, x_amz_client_context, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_client_context_encoding=None) -> web.Response:
    """put_events

    The PutEvents operation records one or more events. You can have up to 1,500 unique custom events per app, any combination of up to 40 attributes and metrics per custom event, and any number of attribute or metric values.

    :param x_amz_client_context: The client context including the client ID, app title, app version and package name.
    :type x_amz_client_context: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_client_context_encoding: The encoding used for the client context.
    :type x_amz_client_context_encoding: str

    """
    body = PutEventsRequest.from_dict(body)
    return web.Response(status=200)
