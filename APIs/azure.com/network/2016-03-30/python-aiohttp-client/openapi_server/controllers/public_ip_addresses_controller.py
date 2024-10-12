from typing import List, Dict
from aiohttp import web

from openapi_server.models.public_ip_address import PublicIPAddress
from openapi_server.models.public_ip_address_list_result import PublicIPAddressListResult
from openapi_server import util


async def public_ip_addresses_create_or_update(request: web.Request, resource_group_name, public_ip_address_name, api_version, subscription_id, parameters) -> web.Response:
    """public_ip_addresses_create_or_update

    The Put PublicIPAddress operation creates/updates a stable/dynamic PublicIP address

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param public_ip_address_name: The name of the publicIpAddress.
    :type public_ip_address_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create/update PublicIPAddress operation
    :type parameters: dict | bytes

    """
    parameters = PublicIPAddress.from_dict(parameters)
    return web.Response(status=200)


async def public_ip_addresses_delete(request: web.Request, resource_group_name, public_ip_address_name, api_version, subscription_id) -> web.Response:
    """public_ip_addresses_delete

    The delete publicIpAddress operation deletes the specified publicIpAddress.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param public_ip_address_name: The name of the subnet.
    :type public_ip_address_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def public_ip_addresses_get(request: web.Request, resource_group_name, public_ip_address_name, api_version, subscription_id, expand=None) -> web.Response:
    """public_ip_addresses_get

    The Get publicIpAddress operation retrieves information about the specified pubicIpAddress

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param public_ip_address_name: The name of the subnet.
    :type public_ip_address_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param expand: expand references resources.
    :type expand: str

    """
    return web.Response(status=200)


async def public_ip_addresses_list(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """public_ip_addresses_list

    The List publicIpAddress operation retrieves all the publicIpAddresses in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def public_ip_addresses_list_all(request: web.Request, api_version, subscription_id) -> web.Response:
    """public_ip_addresses_list_all

    The List publicIpAddress operation retrieves all the publicIpAddresses in a subscription.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
