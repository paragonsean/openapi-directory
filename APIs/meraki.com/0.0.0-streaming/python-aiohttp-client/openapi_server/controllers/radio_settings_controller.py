from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_wireless_rf_profile_request import CreateNetworkWirelessRfProfileRequest
from openapi_server.models.update_network_wireless_rf_profile_request import UpdateNetworkWirelessRfProfileRequest
from openapi_server import util


async def create_network_wireless_rf_profile(request: web.Request, network_id, body) -> web.Response:
    """Creates new RF profile for this network

    Creates new RF profile for this network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkWirelessRfProfileRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_wireless_rf_profile(request: web.Request, network_id, rf_profile_id) -> web.Response:
    """Delete a RF Profile

    Delete a RF Profile

    :param network_id: 
    :type network_id: str
    :param rf_profile_id: 
    :type rf_profile_id: str

    """
    return web.Response(status=200)


async def get_network_wireless_rf_profile(request: web.Request, network_id, rf_profile_id) -> web.Response:
    """Return a RF profile

    Return a RF profile

    :param network_id: 
    :type network_id: str
    :param rf_profile_id: 
    :type rf_profile_id: str

    """
    return web.Response(status=200)


async def get_network_wireless_rf_profiles(request: web.Request, network_id, include_template_profiles=None) -> web.Response:
    """List the non-basic RF profiles for this network

    List the non-basic RF profiles for this network

    :param network_id: 
    :type network_id: str
    :param include_template_profiles: If the network is bound to a template, this parameter controls whether or not the non-basic RF profiles defined on the template should be included in the response alongside the non-basic profiles defined on the bound network. Defaults to false.
    :type include_template_profiles: bool

    """
    return web.Response(status=200)


async def update_network_wireless_rf_profile(request: web.Request, network_id, rf_profile_id, body=None) -> web.Response:
    """Updates specified RF profile for this network

    Updates specified RF profile for this network

    :param network_id: 
    :type network_id: str
    :param rf_profile_id: 
    :type rf_profile_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessRfProfileRequest.from_dict(body)
    return web.Response(status=200)
