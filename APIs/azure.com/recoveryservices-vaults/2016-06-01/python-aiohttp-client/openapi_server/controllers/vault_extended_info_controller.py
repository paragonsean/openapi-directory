from typing import List, Dict
from aiohttp import web

from openapi_server.models.vault_extended_info_resource import VaultExtendedInfoResource
from openapi_server import util


async def vault_extended_info_create_or_update(request: web.Request, subscription_id, resource_group_name, vault_name, api_version, resource_resource_extended_info_details) -> web.Response:
    """vault_extended_info_create_or_update

    Create vault extended info.

    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_resource_extended_info_details: Details of ResourceExtendedInfo
    :type resource_resource_extended_info_details: dict | bytes

    """
    resource_resource_extended_info_details = VaultExtendedInfoResource.from_dict(resource_resource_extended_info_details)
    return web.Response(status=200)


async def vault_extended_info_get(request: web.Request, subscription_id, api_version, resource_group_name, vault_name) -> web.Response:
    """vault_extended_info_get

    Get the vault extended info.

    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str

    """
    return web.Response(status=200)


async def vault_extended_info_update(request: web.Request, subscription_id, resource_group_name, vault_name, api_version, resource_resource_extended_info_details) -> web.Response:
    """vault_extended_info_update

    Update vault extended info.

    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_resource_extended_info_details: Details of ResourceExtendedInfo
    :type resource_resource_extended_info_details: dict | bytes

    """
    resource_resource_extended_info_details = VaultExtendedInfoResource.from_dict(resource_resource_extended_info_details)
    return web.Response(status=200)
