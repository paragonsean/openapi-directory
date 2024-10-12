from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_pii_request_request import CreateNetworkPiiRequestRequest
from openapi_server import util


async def create_network_pii_request_2(request: web.Request, network_id, body=None) -> web.Response:
    """Submit a new delete or restrict processing PII request

    Submit a new delete or restrict processing PII request  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/requests &#x60;&#x60;&#x60;

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkPiiRequestRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_pii_request_2(request: web.Request, network_id, request_id) -> web.Response:
    """Delete a restrict processing PII request

    Delete a restrict processing PII request  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/requests/{requestId} &#x60;&#x60;&#x60;

    :param network_id: 
    :type network_id: str
    :param request_id: 
    :type request_id: str

    """
    return web.Response(status=200)


async def get_network_pii_request_2(request: web.Request, network_id, request_id) -> web.Response:
    """Return a PII request

    Return a PII request  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/requests/{requestId} &#x60;&#x60;&#x60;

    :param network_id: 
    :type network_id: str
    :param request_id: 
    :type request_id: str

    """
    return web.Response(status=200)


async def get_network_pii_requests_2(request: web.Request, network_id) -> web.Response:
    """List the PII requests for this network or organization

    List the PII requests for this network or organization  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/requests &#x60;&#x60;&#x60;

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)
