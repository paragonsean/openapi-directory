from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_all_settings200_response import GetAllSettings200Response
from openapi_server.models.get_allowed_networks200_response import GetAllowedNetworks200Response
from openapi_server.models.get_setting200_response import GetSetting200Response
from openapi_server.models.modify_allowed_networks200_response import ModifyAllowedNetworks200Response
from openapi_server.models.modify_allowed_networks_request import ModifyAllowedNetworksRequest
from openapi_server.models.modify_setting200_response import ModifySetting200Response
from openapi_server.models.modify_setting_request import ModifySettingRequest
from openapi_server.models.set_allowed_networks200_response import SetAllowedNetworks200Response
from openapi_server.models.set_allowed_networks_request import SetAllowedNetworksRequest
from openapi_server import util


async def get_all_settings(request: web.Request, ) -> web.Response:
    """List all settings

    Get the current value of all the settings


    """
    return web.Response(status=200)


async def get_allowed_networks(request: web.Request, node_id) -> web.Response:
    """Get allowed networks for a policy server

    Get the list of allowed networks for a policy server

    :param node_id: Policy server ID for which you want to manage allowed networks.
    :type node_id: str

    """
    return web.Response(status=200)


async def get_setting(request: web.Request, setting_id) -> web.Response:
    """Get the value of a setting

    Get the current value of a specific setting

    :param setting_id: Id of the setting to set
    :type setting_id: str

    """
    return web.Response(status=200)


async def modify_allowed_networks(request: web.Request, node_id, body) -> web.Response:
    """Modify allowed networks for a policy server

    Add or delete allowed networks for a policy server

    :param node_id: Policy server ID for which you want to manage allowed networks.
    :type node_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ModifyAllowedNetworksRequest.from_dict(body)
    return web.Response(status=200)


async def modify_setting(request: web.Request, setting_id, body) -> web.Response:
    """Set the value of a setting

    Set the current value of a specific setting

    :param setting_id: Id of the setting to set
    :type setting_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ModifySettingRequest.from_dict(body)
    return web.Response(status=200)


async def set_allowed_networks(request: web.Request, node_id, body) -> web.Response:
    """Set allowed networks for a policy server

    Set the list of allowed networks for a policy server

    :param node_id: Policy server ID for which you want to manage allowed networks.
    :type node_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SetAllowedNetworksRequest.from_dict(body)
    return web.Response(status=200)
