from typing import List, Dict
from aiohttp import web

from openapi_server.models.applicable_schedule import ApplicableSchedule
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.service_fabric import ServiceFabric
from openapi_server.models.service_fabric_fragment import ServiceFabricFragment
from openapi_server.models.service_fabric_list import ServiceFabricList
from openapi_server import util


async def service_fabrics_create_or_update(request: web.Request, subscription_id, resource_group_name, lab_name, user_name, name, api_version, service_fabric) -> web.Response:
    """service_fabrics_create_or_update

    Create or replace an existing service fabric. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param user_name: The name of the user profile.
    :type user_name: str
    :param name: The name of the service fabric.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param service_fabric: A Service Fabric.
    :type service_fabric: dict | bytes

    """
    service_fabric = ServiceFabric.from_dict(service_fabric)
    return web.Response(status=200)


async def service_fabrics_delete(request: web.Request, subscription_id, resource_group_name, lab_name, user_name, name, api_version) -> web.Response:
    """service_fabrics_delete

    Delete service fabric. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param user_name: The name of the user profile.
    :type user_name: str
    :param name: The name of the service fabric.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def service_fabrics_get(request: web.Request, subscription_id, resource_group_name, lab_name, user_name, name, api_version, expand=None) -> web.Response:
    """service_fabrics_get

    Get service fabric.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param user_name: The name of the user profile.
    :type user_name: str
    :param name: The name of the service fabric.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($expand&#x3D;applicableSchedule)&#39;
    :type expand: str

    """
    return web.Response(status=200)


async def service_fabrics_list(request: web.Request, subscription_id, resource_group_name, lab_name, user_name, api_version, expand=None, filter=None, top=None, orderby=None) -> web.Response:
    """service_fabrics_list

    List service fabrics in a given user profile.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param user_name: The name of the user profile.
    :type user_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($expand&#x3D;applicableSchedule)&#39;
    :type expand: str
    :param filter: The filter to apply to the operation. Example: &#39;$filter&#x3D;contains(name,&#39;myName&#39;)
    :type filter: str
    :param top: The maximum number of resources to return from the operation. Example: &#39;$top&#x3D;10&#39;
    :type top: int
    :param orderby: The ordering expression for the results, using OData notation. Example: &#39;$orderby&#x3D;name desc&#39;
    :type orderby: str

    """
    return web.Response(status=200)


async def service_fabrics_list_applicable_schedules(request: web.Request, subscription_id, resource_group_name, lab_name, user_name, name, api_version) -> web.Response:
    """service_fabrics_list_applicable_schedules

    Lists the applicable start/stop schedules, if any.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param user_name: The name of the user profile.
    :type user_name: str
    :param name: The name of the service fabric.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def service_fabrics_start(request: web.Request, subscription_id, resource_group_name, lab_name, user_name, name, api_version) -> web.Response:
    """service_fabrics_start

    Start a service fabric. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param user_name: The name of the user profile.
    :type user_name: str
    :param name: The name of the service fabric.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def service_fabrics_stop(request: web.Request, subscription_id, resource_group_name, lab_name, user_name, name, api_version) -> web.Response:
    """service_fabrics_stop

    Stop a service fabric This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param user_name: The name of the user profile.
    :type user_name: str
    :param name: The name of the service fabric.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def service_fabrics_update(request: web.Request, subscription_id, resource_group_name, lab_name, user_name, name, api_version, service_fabric) -> web.Response:
    """service_fabrics_update

    Allows modifying tags of service fabrics. All other properties will be ignored.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param user_name: The name of the user profile.
    :type user_name: str
    :param name: The name of the service fabric.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param service_fabric: A Service Fabric.
    :type service_fabric: dict | bytes

    """
    service_fabric = ServiceFabricFragment.from_dict(service_fabric)
    return web.Response(status=200)
