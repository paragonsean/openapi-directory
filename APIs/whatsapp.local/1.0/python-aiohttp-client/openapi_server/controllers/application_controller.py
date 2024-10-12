from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_settings import ApplicationSettings
from openapi_server.models.get_media_providers_response import GetMediaProvidersResponse
from openapi_server.models.media_provider import MediaProvider
from openapi_server.models.response import Response
from openapi_server.models.set_shards_request_body import SetShardsRequestBody
from openapi_server import util


async def delete_media_providers(request: web.Request, provider_name) -> web.Response:
    """Delete-Media-Providers

    

    :param provider_name: Provider Name
    :type provider_name: str

    """
    return web.Response(status=200)


async def get_application_settings(request: web.Request, ) -> web.Response:
    """Get-Application-Settings

    


    """
    return web.Response(status=200)


async def get_media_providers(request: web.Request, ) -> web.Response:
    """Get-Media-Providers

    


    """
    return web.Response(status=200)


async def reset_application_settings(request: web.Request, ) -> web.Response:
    """Reset-Application-Settings

    


    """
    return web.Response(status=200)


async def set_shards(request: web.Request, body) -> web.Response:
    """Set-Shards

    

    :param body: 
    :type body: dict | bytes

    """
    body = SetShardsRequestBody.from_dict(body)
    return web.Response(status=200)


async def update_application_settings(request: web.Request, body) -> web.Response:
    """Update-Application-Settings

    If a field is not present in the request, no change is made to that setting. For example, if on_call_pager is not sent with the request, the existing configuration for on_call_pager is unchanged.

    :param body: 
    :type body: dict | bytes

    """
    body = ApplicationSettings.from_dict(body)
    return web.Response(status=200)


async def update_media_providers(request: web.Request, body) -> web.Response:
    """Update-Media-Providers

    

    :param body: 
    :type body: list | bytes

    """
    body = [MediaProvider.from_dict(d) for d in body]
    return web.Response(status=200)
