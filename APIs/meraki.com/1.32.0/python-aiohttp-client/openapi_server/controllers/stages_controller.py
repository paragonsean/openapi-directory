from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_firmware_upgrades_staged_stages200_response_inner import GetNetworkFirmwareUpgradesStagedStages200ResponseInner
from openapi_server.models.update_network_firmware_upgrades_staged_stages_request import UpdateNetworkFirmwareUpgradesStagedStagesRequest
from openapi_server import util


async def get_network_firmware_upgrades_staged_stages_3(request: web.Request, network_id) -> web.Response:
    """Order of Staged Upgrade Groups in a network

    Order of Staged Upgrade Groups in a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_firmware_upgrades_staged_stages_3(request: web.Request, network_id, body=None) -> web.Response:
    """Assign Staged Upgrade Group order in the sequence.

    Assign Staged Upgrade Group order in the sequence.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkFirmwareUpgradesStagedStagesRequest.from_dict(body)
    return web.Response(status=200)
