from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_stack_collection import ApplicationStackCollection
from openapi_server.models.provider_list_operations200_response import ProviderListOperations200Response
from openapi_server import util


async def provider_get_available_stacks(request: web.Request, api_version, os_type_selected=None) -> web.Response:
    """Get available application frameworks and their versions

    Get available application frameworks and their versions

    :param api_version: API Version
    :type api_version: str
    :param os_type_selected: 
    :type os_type_selected: str

    """
    return web.Response(status=200)


async def provider_get_available_stacks_on_prem(request: web.Request, subscription_id, api_version, os_type_selected=None) -> web.Response:
    """Get available application frameworks and their versions

    Get available application frameworks and their versions

    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param os_type_selected: 
    :type os_type_selected: str

    """
    return web.Response(status=200)


async def provider_list_operations(request: web.Request, api_version) -> web.Response:
    """Gets all available operations for the Microsoft.Web resource provider. Also exposes resource metric definitions

    Gets all available operations for the Microsoft.Web resource provider. Also exposes resource metric definitions

    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)
