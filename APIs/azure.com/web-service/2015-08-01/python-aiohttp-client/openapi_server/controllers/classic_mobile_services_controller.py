from typing import List, Dict
from aiohttp import web

from openapi_server.models.classic_mobile_service import ClassicMobileService
from openapi_server.models.classic_mobile_service_collection import ClassicMobileServiceCollection
from openapi_server import util


async def classic_mobile_services_delete_classic_mobile_service(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Delete a mobile service.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of mobile service
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def classic_mobile_services_get_classic_mobile_service(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get a mobile service.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of mobile service
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def classic_mobile_services_get_classic_mobile_services(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """Get all mobile services in a resource group.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)
