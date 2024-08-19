from typing import List, Dict
from aiohttp import web

from openapi_server.models.na_healthy_home_coach_data_response import NAHealthyHomeCoachDataResponse
from openapi_server import util


async def gethomecoachsdata(request: web.Request, device_id=None) -> web.Response:
    """gethomecoachsdata

    The method gethomecoachsdata Returns data from a user Healthy Home Coach Station (measures and device specific data).

    :param device_id: Id of the device you want to retrieve information of
    :type device_id: str

    """
    return web.Response(status=200)
