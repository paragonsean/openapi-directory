from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_device_switch_warm_spare_request import UpdateDeviceSwitchWarmSpareRequest
from openapi_server.models.update_network_appliance_warm_spare_request import UpdateNetworkApplianceWarmSpareRequest
from openapi_server import util


async def get_device_switch_warm_spare_1(request: web.Request, serial) -> web.Response:
    """Return warm spare configuration for a switch

    Return warm spare configuration for a switch

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_network_appliance_warm_spare_1(request: web.Request, network_id) -> web.Response:
    """Return MX warm spare settings

    Return MX warm spare settings

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def swap_network_appliance_warm_spare_1(request: web.Request, network_id) -> web.Response:
    """Swap MX primary and warm spare appliances

    Swap MX primary and warm spare appliances

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_device_switch_warm_spare_1(request: web.Request, serial, body) -> web.Response:
    """Update warm spare configuration for a switch

    Update warm spare configuration for a switch. The spare will use the same L3 configuration as the primary. Note that this will irreversibly destroy any existing L3 configuration on the spare.

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceSwitchWarmSpareRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_warm_spare_1(request: web.Request, network_id, body) -> web.Response:
    """Update MX warm spare settings

    Update MX warm spare settings

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceWarmSpareRequest.from_dict(body)
    return web.Response(status=200)
