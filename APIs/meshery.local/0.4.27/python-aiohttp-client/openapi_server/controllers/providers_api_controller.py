from typing import List, Dict
from aiohttp import web

from openapi_server.models.provider_properties import ProviderProperties
from openapi_server import util


async def id_choice_provider(request: web.Request, provider=None) -> web.Response:
    """Handle GET request for the choice of provider

    Update the choice of provider in system

    :param provider: 
    :type provider: str

    """
    return web.Response(status=200)


async def id_get_provider_capabilities(request: web.Request, ) -> web.Response:
    """Handle GET requests for Provider

    Returns the capabilities.json for the provider


    """
    return web.Response(status=200)


async def id_get_providers_list(request: web.Request, ) -> web.Response:
    """Handle GET request for list of providers

    Returns the available list of providers


    """
    return web.Response(status=200)


async def id_provider(request: web.Request, ) -> web.Response:
    """Handle GET request to provider UI

    Servers providers UI


    """
    return web.Response(status=200)


async def id_react_components(request: web.Request, ) -> web.Response:
    """Handle GET request for React Components

    handles the requests to serve react components from the provider package


    """
    return web.Response(status=200)
