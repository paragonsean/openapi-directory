from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_session_response import CreateSessionResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.session import Session
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server import util


async def sessions_create(request: web.Request, x_apideck_consumer_id, x_apideck_app_id, body=None) -> web.Response:
    """Create Session

    Making a POST request to this endpoint will initiate a Hosted Vault session. Redirect the consumer to the returned URL to allow temporary access to manage their integrations and settings.  Note: This is a short lived token that will expire after 1 hour (TTL: 3600). 

    :param x_apideck_consumer_id: ID of the consumer which you want to get or push data from
    :type x_apideck_consumer_id: str
    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param body: Additional redirect uri and/or consumer metadata
    :type body: dict | bytes

    """
    body = Session.from_dict(body)
    return web.Response(status=200)
