from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response400_bad_admin_or_value import ErrorResponse400BadAdminOrValue
from openapi_server.models.error_response401_bad_key_for_basic_auth import ErrorResponse401BadKeyForBasicAuth
from openapi_server.models.strategy_response import StrategyResponse
from openapi_server import util


async def read_strategy_details_0(request: web.Request, ) -> web.Response:
    """read_strategy_details_0

    Returns the name, date, time, and CRC of the strategy currently in the controller, and the number of charts currently running. Empty strings and a 0 will be returned when there is no strategy.


    """
    return web.Response(status=200)
