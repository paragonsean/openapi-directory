from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.vault import Vault
from openapi_server import util


async def get_vault_by_id(request: web.Request, vault_uuid) -> web.Response:
    """Get Vault details and metadata

    

    :param vault_uuid: The UUID of the Vault to fetch Items from
    :type vault_uuid: str

    """
    return web.Response(status=200)


async def get_vaults(request: web.Request, filter=None) -> web.Response:
    """Get all Vaults

    

    :param filter: Filter the Vault collection based on Vault name using SCIM eq filter
    :type filter: str

    """
    return web.Response(status=200)
