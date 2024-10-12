from typing import List, Dict
from aiohttp import web

from openapi_server.models.api import API
from openapi_server.models.get_providers200_response import GetProviders200Response
from openapi_server.models.get_services200_response import GetServices200Response
from openapi_server.models.metrics import Metrics
from openapi_server import util


async def get_api(request: web.Request, provider, api) -> web.Response:
    """Retrieve one version of a particular API

    Returns the API entry for one specific version of an API where there is no serviceName.

    :param provider: 
    :type provider: str
    :param api: 
    :type api: str

    """
    return web.Response(status=200)


async def get_metrics(request: web.Request, ) -> web.Response:
    """Get basic metrics

    Some basic metrics for the entire directory. Just stunning numbers to put on a front page and are intended purely for WoW effect :) 


    """
    return web.Response(status=200)


async def get_provider(request: web.Request, provider) -> web.Response:
    """List all APIs for a particular provider

    List all APIs in the directory for a particular providerName Returns links to the individual API entry for each API. 

    :param provider: 
    :type provider: str

    """
    return web.Response(status=200)


async def get_providers(request: web.Request, ) -> web.Response:
    """List all providers

    List all the providers in the directory 


    """
    return web.Response(status=200)


async def get_service_api(request: web.Request, provider, service, api) -> web.Response:
    """Retrieve one version of a particular API with a serviceName.

    Returns the API entry for one specific version of an API where there is a serviceName.

    :param provider: 
    :type provider: str
    :param service: 
    :type service: str
    :param api: 
    :type api: str

    """
    return web.Response(status=200)


async def get_services(request: web.Request, provider) -> web.Response:
    """List all serviceNames for a particular provider

    List all serviceNames in the directory for a particular providerName 

    :param provider: 
    :type provider: str

    """
    return web.Response(status=200)


async def list_apis(request: web.Request, ) -> web.Response:
    """List all APIs

    List all APIs in the directory. Returns links to the OpenAPI definitions for each API in the directory. If API exist in multiple versions &#x60;preferred&#x60; one is explicitly marked. Some basic info from the OpenAPI definition is cached inside each object. This allows you to generate some simple views without needing to fetch the OpenAPI definition for each API. 


    """
    return web.Response(status=200)
