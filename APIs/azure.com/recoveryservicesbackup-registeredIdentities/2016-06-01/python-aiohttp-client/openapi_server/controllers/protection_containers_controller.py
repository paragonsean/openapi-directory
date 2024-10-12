from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def protection_containers_unregister(request: web.Request, subscription_id, resource_group_name, vault_name, api_version, identity_name) -> web.Response:
    """protection_containers_unregister

    Unregisters the given container from your Recovery Services vault.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group associated with the Recovery Services vault.
    :type resource_group_name: str
    :param vault_name: The name of the Recovery Services vault.
    :type vault_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param identity_name: Name of the protection container to unregister.
    :type identity_name: str

    """
    return web.Response(status=200)
