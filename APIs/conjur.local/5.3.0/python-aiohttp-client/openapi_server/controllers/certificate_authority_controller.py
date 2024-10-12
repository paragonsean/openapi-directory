from typing import List, Dict
from aiohttp import web

from openapi_server.models.sign201_response import Sign201Response
from openapi_server import util


async def sign(request: web.Request, account, service_id, csr, ttl, x_request_id=None, accept=None) -> web.Response:
    """Gets a signed certificate from the configured Certificate Authority service.

    Gets a signed certificate from the configured Certificate Authority service.  The request must include a valid Certificate Signing Request, and a desired TTL in ISO 8601 format.  *** IMPORTANT *** This endpoint is part of an early implementation of support for using Conjur as a certificate authority, and is currently available at the Community (or early alpha) level. This endpoint is still subject to breaking changes in the future. 

    :param account: Organization account name
    :type account: str
    :param service_id: Name of the Certificate Authority service
    :type service_id: str
    :param csr: 
    :type csr: str
    :param ttl: 
    :type ttl: str
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str
    :param accept: Setting the Accept header to &#x60;application/x-pem-file&#x60; allows Conjur to respond with a formatted certificate
    :type accept: str

    """
    return web.Response(status=200)
