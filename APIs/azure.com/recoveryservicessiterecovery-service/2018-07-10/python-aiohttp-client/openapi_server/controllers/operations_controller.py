from typing import List, Dict
from aiohttp import web

from openapi_server.models.operations_discovery_collection import OperationsDiscoveryCollection
from openapi_server import util


async def operations_list(request: web.Request, api_version, resource_group_name, subscription_id) -> web.Response:
    """Returns the list of available operations.

    Operation to return the list of available operations.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str

    """
    return web.Response(status=200)
