from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_capacity_name_availability_parameters import CheckCapacityNameAvailabilityParameters
from openapi_server.models.check_capacity_name_availability_result import CheckCapacityNameAvailabilityResult
from openapi_server.models.dedicated_capacities import DedicatedCapacities
from openapi_server.models.dedicated_capacity import DedicatedCapacity
from openapi_server.models.dedicated_capacity_update_parameters import DedicatedCapacityUpdateParameters
from openapi_server.models.sku_enumeration_for_existing_resource_result import SkuEnumerationForExistingResourceResult
from openapi_server import util


async def capacities_check_name_availability(request: web.Request, location, api_version, subscription_id, capacity_parameters) -> web.Response:
    """capacities_check_name_availability

    Check the name availability in the target location.

    :param location: The region name which the operation will lookup into.
    :type location: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param capacity_parameters: The name of the capacity.
    :type capacity_parameters: dict | bytes

    """
    capacity_parameters = CheckCapacityNameAvailabilityParameters.from_dict(capacity_parameters)
    return web.Response(status=200)


async def capacities_create(request: web.Request, resource_group_name, dedicated_capacity_name, api_version, subscription_id, capacity_parameters) -> web.Response:
    """capacities_create

    Provisions the specified Dedicated capacity based on the configuration specified in the request.

    :param resource_group_name: The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
    :type resource_group_name: str
    :param dedicated_capacity_name: The name of the Dedicated capacity. It must be a minimum of 3 characters, and a maximum of 63.
    :type dedicated_capacity_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param capacity_parameters: Contains the information used to provision the Dedicated capacity.
    :type capacity_parameters: dict | bytes

    """
    capacity_parameters = DedicatedCapacity.from_dict(capacity_parameters)
    return web.Response(status=200)


async def capacities_delete(request: web.Request, resource_group_name, dedicated_capacity_name, api_version, subscription_id) -> web.Response:
    """capacities_delete

    Deletes the specified Dedicated capacity.

    :param resource_group_name: The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
    :type resource_group_name: str
    :param dedicated_capacity_name: The name of the Dedicated capacity. It must be at least 3 characters in length, and no more than 63.
    :type dedicated_capacity_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def capacities_get_details(request: web.Request, resource_group_name, dedicated_capacity_name, api_version, subscription_id) -> web.Response:
    """capacities_get_details

    Gets details about the specified dedicated capacity.

    :param resource_group_name: The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
    :type resource_group_name: str
    :param dedicated_capacity_name: The name of the dedicated capacity. It must be a minimum of 3 characters, and a maximum of 63.
    :type dedicated_capacity_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def capacities_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """capacities_list

    Lists all the Dedicated capacities for the given subscription.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def capacities_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """capacities_list_by_resource_group

    Gets all the Dedicated capacities for the given resource group.

    :param resource_group_name: The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
    :type resource_group_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def capacities_list_skus_for_capacity(request: web.Request, resource_group_name, dedicated_capacity_name, api_version, subscription_id) -> web.Response:
    """capacities_list_skus_for_capacity

    Lists eligible SKUs for a PowerBI Dedicated resource.

    :param resource_group_name: The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
    :type resource_group_name: str
    :param dedicated_capacity_name: The name of the Dedicated capacity. It must be at least 3 characters in length, and no more than 63.
    :type dedicated_capacity_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def capacities_resume(request: web.Request, resource_group_name, dedicated_capacity_name, api_version, subscription_id) -> web.Response:
    """capacities_resume

    Resumes operation of the specified Dedicated capacity instance.

    :param resource_group_name: The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
    :type resource_group_name: str
    :param dedicated_capacity_name: The name of the Dedicated capacity. It must be at least 3 characters in length, and no more than 63.
    :type dedicated_capacity_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def capacities_suspend(request: web.Request, resource_group_name, dedicated_capacity_name, api_version, subscription_id) -> web.Response:
    """capacities_suspend

    Suspends operation of the specified dedicated capacity instance.

    :param resource_group_name: The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
    :type resource_group_name: str
    :param dedicated_capacity_name: The name of the Dedicated capacity. It must be at least 3 characters in length, and no more than 63.
    :type dedicated_capacity_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def capacities_update(request: web.Request, resource_group_name, dedicated_capacity_name, api_version, subscription_id, capacity_update_parameters) -> web.Response:
    """capacities_update

    Updates the current state of the specified Dedicated capacity.

    :param resource_group_name: The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
    :type resource_group_name: str
    :param dedicated_capacity_name: The name of the Dedicated capacity. It must be at least 3 characters in length, and no more than 63.
    :type dedicated_capacity_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param capacity_update_parameters: Request object that contains the updated information for the capacity.
    :type capacity_update_parameters: dict | bytes

    """
    capacity_update_parameters = DedicatedCapacityUpdateParameters.from_dict(capacity_update_parameters)
    return web.Response(status=200)
