from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.create_device_request import CreateDeviceRequest
from openapi_server.models.list_push_providers_response import ListPushProvidersResponse
from openapi_server.models.response import Response
from openapi_server.models.upsert_push_provider_request import UpsertPushProviderRequest
from openapi_server.models.upsert_push_provider_response import UpsertPushProviderResponse
from openapi_server import util


async def create_device_0(request: web.Request, body) -> web.Response:
    """Create device

    Adds a new device to a user, if the same device already exists the call will have no effect 

    :param body: 
    :type body: dict | bytes

    """
    body = CreateDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def delete_push_provider(request: web.Request, type, name) -> web.Response:
    """Delete a push provider

    Delete a push provider from v2 with multi bundle/package support. v1 isn&#39;t supported in this endpoint 

    :param type: 
    :type type: str
    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def list_push_providers(request: web.Request, ) -> web.Response:
    """List push providers

    List details of all push providers. 


    """
    return web.Response(status=200)


async def upsert_push_provider(request: web.Request, body) -> web.Response:
    """Upsert a push provider

    Upsert a push provider for v2 with multi bundle/package support 

    :param body: 
    :type body: dict | bytes

    """
    body = UpsertPushProviderRequest.from_dict(body)
    return web.Response(status=200)
