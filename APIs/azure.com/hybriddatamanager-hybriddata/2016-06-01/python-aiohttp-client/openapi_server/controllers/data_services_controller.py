from typing import List, Dict
from aiohttp import web

from openapi_server.models.data_service import DataService
from openapi_server.models.data_service_list import DataServiceList
from openapi_server import util


async def data_services_get(request: web.Request, data_service_name, subscription_id, resource_group_name, data_manager_name, api_version) -> web.Response:
    """data_services_get

    Gets the data service that match the data service name given.

    :param data_service_name: The name of the data service that is being queried.
    :type data_service_name: str
    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param data_manager_name: The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    :type data_manager_name: str
    :param api_version: The API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def data_services_list_by_data_manager(request: web.Request, subscription_id, resource_group_name, data_manager_name, api_version) -> web.Response:
    """data_services_list_by_data_manager

    This method gets all the data services.

    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param data_manager_name: The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    :type data_manager_name: str
    :param api_version: The API Version
    :type api_version: str

    """
    return web.Response(status=200)
