from typing import List, Dict
from aiohttp import web

from openapi_server.models.wimstatus200_response import Wimstatus200Response
from openapi_server import util


async def wimstatus(request: web.Request, vid=None) -> web.Response:
    """WiM Proess Informtion

    Access to status information of an existing metering change and allocation process. 

    :param vid: VID key of the process.
    :type vid: str

    """
    return web.Response(status=200)
