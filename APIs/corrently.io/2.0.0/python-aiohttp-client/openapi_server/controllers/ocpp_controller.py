from typing import List, Dict
from aiohttp import web

from openapi_server.models.easee_charger import EaseeCharger
from openapi_server import util


async def ocpp_sessions(request: web.Request, ) -> web.Response:
    """Last Session Info

    Returns lastSession info of OCCP Cloud service for clearing in corrently ecosystem. Might be tested via [OCPP cloud simulator](https://ocpp.corrently.cloud). Last session Info of managed EV charging stations connected to the correnty ecosystem. 


    """
    return web.Response(status=200)
