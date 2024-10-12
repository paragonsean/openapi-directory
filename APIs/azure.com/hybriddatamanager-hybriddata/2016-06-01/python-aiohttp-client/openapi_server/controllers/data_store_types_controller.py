from typing import List, Dict
from aiohttp import web

from openapi_server.models.data_store_type import DataStoreType
from openapi_server.models.data_store_type_list import DataStoreTypeList
from openapi_server import util


async def data_store_types_get(request: web.Request, data_store_type_name, subscription_id, resource_group_name, data_manager_name, api_version) -> web.Response:
    """data_store_types_get

    Gets the data store/repository type given its name.

    :param data_store_type_name: The data store/repository type name for which details are needed.
    :type data_store_type_name: str
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


async def data_store_types_list_by_data_manager(request: web.Request, subscription_id, resource_group_name, data_manager_name, api_version) -> web.Response:
    """data_store_types_list_by_data_manager

    Gets all the data store/repository types that the resource supports.

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
