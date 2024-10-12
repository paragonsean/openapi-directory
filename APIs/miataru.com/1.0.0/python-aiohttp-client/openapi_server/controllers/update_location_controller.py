from typing import List, Dict
from aiohttp import web

from openapi_server.models.ack import ACK
from openapi_server.models.miataru_update_location_request import MiataruUpdateLocationRequest
from openapi_server import util


async def update_location(request: web.Request, body) -> web.Response:
    """update_location

    This method is used to update the location of a device. The device does not need to be known already to the Miataru server but it rather creates a unique identifier for itself in the client application. This unique identifier, or device ID is then used to address this particular device.

    :param body: the body of this UpdateLocation POST request contains the JSON formatted parameters.
    :type body: dict | bytes

    """
    body = MiataruUpdateLocationRequest.from_dict(body)
    return web.Response(status=200)
