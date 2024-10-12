from typing import List, Dict
from aiohttp import web

from openapi_server.models.dataset_list_response import DatasetListResponse
from openapi_server.models.dataset_resource import DatasetResource
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def datasets_create_or_update(request: web.Request, subscription_id, resource_group_name, factory_name, dataset_name, api_version, dataset, if_match=None) -> web.Response:
    """datasets_create_or_update

    Creates or updates a dataset.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param dataset_name: The dataset name.
    :type dataset_name: str
    :param api_version: The API version.
    :type api_version: str
    :param dataset: Dataset resource definition.
    :type dataset: dict | bytes
    :param if_match: ETag of the dataset entity.  Should only be specified for update, for which it should match existing entity or can be * for unconditional update.
    :type if_match: str

    """
    dataset = DatasetResource.from_dict(dataset)
    return web.Response(status=200)


async def datasets_delete(request: web.Request, subscription_id, resource_group_name, factory_name, dataset_name, api_version) -> web.Response:
    """datasets_delete

    Deletes a dataset.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param dataset_name: The dataset name.
    :type dataset_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def datasets_get(request: web.Request, subscription_id, resource_group_name, factory_name, dataset_name, api_version) -> web.Response:
    """datasets_get

    Gets a dataset.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param dataset_name: The dataset name.
    :type dataset_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def datasets_list_by_factory(request: web.Request, subscription_id, resource_group_name, factory_name, api_version) -> web.Response:
    """datasets_list_by_factory

    Lists datasets.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)
