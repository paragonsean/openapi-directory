from typing import List, Dict
from aiohttp import web

from openapi_server.models.tenant_access_update_default_response import TenantAccessUpdateDefaultResponse
from openapi_server import util


async def tenant_policy_create_or_update(request: web.Request, resource_group_name, service_name, if_match, api_version, subscription_id, parameters) -> web.Response:
    """tenant_policy_create_or_update

    Creates or updates global policy configuration for the tenant.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param if_match: The entity state (Etag) version of the tenant policy to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The policy content details.
    :type parameters: 

    """
    return web.Response(status=200)


async def tenant_policy_delete(request: web.Request, resource_group_name, service_name, if_match, api_version, subscription_id) -> web.Response:
    """tenant_policy_delete

    Deletes the global tenant policy configuration.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param if_match: The entity state (Etag) version of the tenant policy to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def tenant_policy_get(request: web.Request, resource_group_name, service_name, api_version, subscription_id) -> web.Response:
    """tenant_policy_get

    Get the global policy configuration of the tenant.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
