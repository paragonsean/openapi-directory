from typing import List, Dict
from aiohttp import web

from openapi_server.models.tenant_configuration_sync_state_contract import TenantConfigurationSyncStateContract
from openapi_server import util


async def tenant_configuration_get_sync_state(request: web.Request, api_version, configuration_name) -> web.Response:
    """tenant_configuration_get_sync_state

    Gets the status of the most recent synchronization between the configuration database and the Git repository.

    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param configuration_name: The identifier of the Git Configuration Operation.
    :type configuration_name: str

    """
    return web.Response(status=200)
