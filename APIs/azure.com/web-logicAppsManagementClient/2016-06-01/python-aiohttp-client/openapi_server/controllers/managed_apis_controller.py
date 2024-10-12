from typing import List, Dict
from aiohttp import web

from openapi_server.models.managed_api_definition import ManagedApiDefinition
from openapi_server.models.managed_api_definition_collection import ManagedApiDefinitionCollection
from openapi_server import util


async def managed_apis_get(request: web.Request, subscription_id, location, api_name, api_version) -> web.Response:
    """Gets managed API

    Gets a managed API

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param location: The location
    :type location: str
    :param api_name: API name
    :type api_name: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def managed_apis_list(request: web.Request, location, subscription_id, api_version) -> web.Response:
    """Lists managed APIs

    Gets a list of managed APIs

    :param location: The location
    :type location: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)
