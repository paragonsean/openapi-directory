from typing import List, Dict
from aiohttp import web

from openapi_server.models.tenant_configuration_sync_state_contract import TenantConfigurationSyncStateContract
from openapi_server import util


async def tenant_configuration_get_sync_state(request: web.Request, resource_group_name, service_name, api_version, subscription_id, configuration_name) -> web.Response:
    """tenant_configuration_get_sync_state

    Gets the status of the most recent synchronization between the configuration database and the Git repository.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param configuration_name: The identifier of the Git Configuration Operation.
    :type configuration_name: str

    """
    return web.Response(status=200)
