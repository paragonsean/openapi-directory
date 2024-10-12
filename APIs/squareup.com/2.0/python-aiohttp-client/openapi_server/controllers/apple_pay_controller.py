from typing import List, Dict
from aiohttp import web

from openapi_server.models.register_domain_request import RegisterDomainRequest
from openapi_server.models.register_domain_response import RegisterDomainResponse
from openapi_server import util


async def register_domain(request: web.Request, body) -> web.Response:
    """RegisterDomain

    Activates a domain for use with Apple Pay on the Web and Square. A validation is performed on this domain by Apple to ensure that it is properly set up as an Apple Pay enabled domain.  This endpoint provides an easy way for platform developers to bulk activate Apple Pay on the Web with Square for merchants using their platform.  To learn more about Web Apple Pay, see [Add the Apple Pay on the Web Button](https://developer.squareup.com/docs/payment-form/add-digital-wallets/apple-pay).

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = RegisterDomainRequest.from_dict(body)
    return web.Response(status=200)
