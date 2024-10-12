from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_sm_devices_fields200_response_inner import UpdateNetworkSmDevicesFields200ResponseInner
from openapi_server.models.update_network_sm_devices_fields_request import UpdateNetworkSmDevicesFieldsRequest
from openapi_server import util


async def update_network_sm_devices_fields_2(request: web.Request, network_id, body) -> web.Response:
    """Modify the fields of a device

    Modify the fields of a device

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSmDevicesFieldsRequest.from_dict(body)
    return web.Response(status=200)
