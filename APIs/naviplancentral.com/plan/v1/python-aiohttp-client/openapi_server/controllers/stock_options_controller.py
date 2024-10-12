from typing import List, Dict
from aiohttp import web

from openapi_server.models.stock_option_model import StockOptionModel
from openapi_server.models.stock_options_model import StockOptionsModel
from openapi_server import util


async def stock_options_get_by_id_planid(request: web.Request, id, plan_id) -> web.Response:
    """Retrieve a stock option

    This operation retrieves a stock option from the plan.

    :param id: ID of stock option to retrieve
    :type id: int
    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)


async def stock_options_get_by_planid(request: web.Request, plan_id) -> web.Response:
    """Retrieve stock options

    This operation retrieves a list of all of the stock options in the plan.

    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)
