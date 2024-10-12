from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_switch_dscp_to_cos_mappings_request import UpdateNetworkSwitchDscpToCosMappingsRequest
from openapi_server import util


async def get_network_switch_dscp_to_cos_mappings_1(request: web.Request, network_id) -> web.Response:
    """Return the DSCP to CoS mappings

    Return the DSCP to CoS mappings

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_switch_dscp_to_cos_mappings_1(request: web.Request, network_id, body) -> web.Response:
    """Update the DSCP to CoS mappings

    Update the DSCP to CoS mappings

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchDscpToCosMappingsRequest.from_dict(body)
    return web.Response(status=200)
