from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_information_contract import AccessInformationContract
from openapi_server.models.access_information_update_parameters import AccessInformationUpdateParameters
from openapi_server.models.tenant_access_update_default_response import TenantAccessUpdateDefaultResponse
from openapi_server import util


async def tenant_access_get(request: web.Request, resource_group_name, service_name, api_version, subscription_id, access_name) -> web.Response:
    """tenant_access_get

    Get tenant access information details.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param access_name: The identifier of the Access configuration.
    :type access_name: str

    """
    return web.Response(status=200)


async def tenant_access_regenerate_primary_key(request: web.Request, resource_group_name, service_name, api_version, subscription_id, access_name) -> web.Response:
    """tenant_access_regenerate_primary_key

    Regenerate primary access key.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param access_name: The identifier of the Access configuration.
    :type access_name: str

    """
    return web.Response(status=200)


async def tenant_access_regenerate_secondary_key(request: web.Request, resource_group_name, service_name, api_version, subscription_id, access_name) -> web.Response:
    """tenant_access_regenerate_secondary_key

    Regenerate secondary access key.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param access_name: The identifier of the Access configuration.
    :type access_name: str

    """
    return web.Response(status=200)


async def tenant_access_update(request: web.Request, resource_group_name, service_name, access_name, if_match, api_version, subscription_id, parameters) -> web.Response:
    """tenant_access_update

    Update tenant access information details.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param access_name: The identifier of the Access configuration.
    :type access_name: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to retrieve the Tenant Access Information.
    :type parameters: dict | bytes

    """
    parameters = AccessInformationUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
