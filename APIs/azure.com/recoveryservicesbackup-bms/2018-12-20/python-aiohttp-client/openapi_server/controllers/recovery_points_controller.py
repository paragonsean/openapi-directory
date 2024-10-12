from typing import List, Dict
from aiohttp import web

from openapi_server.models.crr_access_token_resource import CrrAccessTokenResource
from openapi_server import util


async def recovery_points_get_access_token(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, container_name, protected_item_name, recovery_point_id) -> web.Response:
    """Returns the Access token for communication between BMS and Protection service

    

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name associated with the container.
    :type fabric_name: str
    :param container_name: Name of the container.
    :type container_name: str
    :param protected_item_name: Name of the Protected Item.
    :type protected_item_name: str
    :param recovery_point_id: Recovery Point Id
    :type recovery_point_id: str

    """
    return web.Response(status=200)
