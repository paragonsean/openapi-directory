from typing import List, Dict
from aiohttp import web

from openapi_server.models.farm import Farm
from openapi_server.models.farm_creation_properties import FarmCreationProperties
from openapi_server.models.farm_list import FarmList
from openapi_server.models.farms_list_metric_definitions200_response import FarmsListMetricDefinitions200Response
from openapi_server.models.farms_list_metrics200_response import FarmsListMetrics200Response
from openapi_server import util


async def farms_create(request: web.Request, subscription_id, resource_group_name, farm_id, api_version, farm_object) -> web.Response:
    """farms_create

    Create a new storage farm.

    :param subscription_id: Subscription Id.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param farm_id: Farm Id.
    :type farm_id: str
    :param api_version: REST Api Version.
    :type api_version: str
    :param farm_object: Parameters used to create a farm
    :type farm_object: dict | bytes

    """
    farm_object = FarmCreationProperties.from_dict(farm_object)
    return web.Response(status=200)


async def farms_get(request: web.Request, subscription_id, resource_group_name, farm_id, api_version) -> web.Response:
    """farms_get

    Returns the Storage properties and settings for a specified storage farm.

    :param subscription_id: Subscription Id.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param farm_id: Farm Id.
    :type farm_id: str
    :param api_version: REST Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def farms_list(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """farms_list

    Returns a list of all storage farms.

    :param subscription_id: Subscription Id.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param api_version: REST Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def farms_list_metric_definitions(request: web.Request, subscription_id, resource_group_name, farm_id, api_version) -> web.Response:
    """farms_list_metric_definitions

    Returns a list of metric definitions for a storage farm.

    :param subscription_id: Subscription Id.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param farm_id: Farm Id.
    :type farm_id: str
    :param api_version: REST Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def farms_list_metrics(request: web.Request, subscription_id, resource_group_name, farm_id, api_version) -> web.Response:
    """farms_list_metrics

    Returns a list of storage farm metrics.

    :param subscription_id: Subscription Id.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param farm_id: Farm Id.
    :type farm_id: str
    :param api_version: REST Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def farms_start_garbage_collection(request: web.Request, subscription_id, resource_group_name, farm_id, api_version) -> web.Response:
    """farms_start_garbage_collection

    Start garbage collection on deleted storage objects.

    :param subscription_id: Subscription Id.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param farm_id: Farm Id.
    :type farm_id: str
    :param api_version: REST Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def farms_update(request: web.Request, subscription_id, api_version, resource_group_name, farm_id, farm_object) -> web.Response:
    """farms_update

    Update an existing storage farm.

    :param subscription_id: Subscription Id.
    :type subscription_id: str
    :param api_version: REST Api Version.
    :type api_version: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param farm_id: Farm Id.
    :type farm_id: str
    :param farm_object: Farm to update.
    :type farm_object: dict | bytes

    """
    farm_object = Farm.from_dict(farm_object)
    return web.Response(status=200)
