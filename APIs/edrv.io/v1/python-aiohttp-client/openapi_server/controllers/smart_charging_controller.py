from typing import List, Dict
from aiohttp import web

from openapi_server.models.deletechargingschedule_request import DeletechargingscheduleRequest
from openapi_server.models.setchargingschedule201_response import Setchargingschedule201Response
from openapi_server.models.setchargingschedule_request import SetchargingscheduleRequest
from openapi_server import util


async def deletechargingschedule(request: web.Request, body) -> web.Response:
    """deletechargingschedule

    Delete a smart charging schedule

    :param body: 
    :type body: dict | bytes

    """
    body = DeletechargingscheduleRequest.from_dict(body)
    return web.Response(status=200)


async def setchargingschedule(request: web.Request, body) -> web.Response:
    """setchargingschedule

    Set one of charging power or current of a specific chargestation connector

    :param body: 
    :type body: dict | bytes

    """
    body = SetchargingscheduleRequest.from_dict(body)
    return web.Response(status=200)
