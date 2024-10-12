from typing import List, Dict
from aiohttp import web

from openapi_server.models.data_store import DataStore
from openapi_server.models.data_store_list import DataStoreList
from openapi_server import util


async def data_stores_create_or_update(request: web.Request, data_store_name, subscription_id, resource_group_name, data_manager_name, api_version, data_store) -> web.Response:
    """data_stores_create_or_update

    Creates or updates the data store/repository in the data manager.

    :param data_store_name: The data store/repository name to be created or updated.
    :type data_store_name: str
    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param data_manager_name: The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    :type data_manager_name: str
    :param api_version: The API Version
    :type api_version: str
    :param data_store: The data store/repository object to be created or updated.
    :type data_store: dict | bytes

    """
    data_store = DataStore.from_dict(data_store)
    return web.Response(status=200)


async def data_stores_delete(request: web.Request, data_store_name, subscription_id, resource_group_name, data_manager_name, api_version) -> web.Response:
    """data_stores_delete

    This method deletes the given data store/repository.

    :param data_store_name: The data store/repository name to be deleted.
    :type data_store_name: str
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


async def data_stores_get(request: web.Request, data_store_name, subscription_id, resource_group_name, data_manager_name, api_version) -> web.Response:
    """data_stores_get

    This method gets the data store/repository by name.

    :param data_store_name: The data store/repository name queried.
    :type data_store_name: str
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


async def data_stores_list_by_data_manager(request: web.Request, subscription_id, resource_group_name, data_manager_name, api_version, filter=None) -> web.Response:
    """data_stores_list_by_data_manager

    Gets all the data stores/repositories in the given resource.

    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param data_manager_name: The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    :type data_manager_name: str
    :param api_version: The API Version
    :type api_version: str
    :param filter: OData Filter options
    :type filter: str

    """
    return web.Response(status=200)
