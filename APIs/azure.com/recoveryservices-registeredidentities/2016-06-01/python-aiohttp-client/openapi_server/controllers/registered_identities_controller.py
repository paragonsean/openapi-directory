from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def registered_identities_delete(request: web.Request, subscription_id, api_version, resource_group_name, vault_name, identity_name) -> web.Response:
    """registered_identities_delete

    Unregisters the given container from your Recovery Services vault.

    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param identity_name: Name of the protection container to unregister.
    :type identity_name: str

    """
    return web.Response(status=200)
