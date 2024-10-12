from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_sm_device_cellular_usage_history200_response_inner import GetNetworkSmDeviceCellularUsageHistory200ResponseInner
from openapi_server import util


async def get_network_sm_device_cellular_usage_history_2(request: web.Request, network_id, device_id) -> web.Response:
    """Return the client&#39;s daily cellular data usage history

    Return the client&#39;s daily cellular data usage history. Usage data is in kilobytes.

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)
