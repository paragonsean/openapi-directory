from typing import List, Dict
from aiohttp import web

from openapi_server.models.token_information import TokenInformation
from openapi_server import util


async def security_pins_get(request: web.Request, api_version, vault_name, resource_group_name, subscription_id) -> web.Response:
    """security_pins_get

    Get the security PIN.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str

    """
    return web.Response(status=200)
