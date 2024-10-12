from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_firmware_upgrades_rollback200_response import CreateNetworkFirmwareUpgradesRollback200Response
from openapi_server.models.create_network_firmware_upgrades_rollback_request import CreateNetworkFirmwareUpgradesRollbackRequest
from openapi_server import util


async def create_network_firmware_upgrades_rollback_2(request: web.Request, network_id, body) -> web.Response:
    """Rollback a Firmware Upgrade For A Network

    Rollback a Firmware Upgrade For A Network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkFirmwareUpgradesRollbackRequest.from_dict(body)
    return web.Response(status=200)
