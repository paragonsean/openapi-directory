from typing import List, Dict
from aiohttp import web

from openapi_server.models.metering_get200_response import MeteringGet200Response
from openapi_server.models.metering_post200_response import MeteringPost200Response
from openapi_server.models.metering_post_request import MeteringPostRequest
from openapi_server import util


async def metering_get(request: web.Request, account=None) -> web.Response:
    """Meter Reading

    Retrieves a metered reading using account (Stromkonto). 

    :param account: Account/Address (Stromkonto) to retrieve reading for.
    :type account: str

    """
    return web.Response(status=200)


async def metering_post(request: web.Request, body) -> web.Response:
    """Meter Reading

    Post meter reading and get it decorated. Best practice is to first create a new Stromkonto with the register method and choose a nice secret to protect updates. Now regularly send updates to get readings (consumption) split into green power (1.8.1) and grey power (1.8.2). 

    :param body: 
    :type body: dict | bytes

    """
    body = MeteringPostRequest.from_dict(body)
    return web.Response(status=200)
