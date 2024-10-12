from typing import List, Dict
from aiohttp import web

from openapi_server.models.restricted_stock_model import RestrictedStockModel
from openapi_server.models.restricted_stocks_model import RestrictedStocksModel
from openapi_server import util


async def restricted_stocks_get_by_id_planid(request: web.Request, id, plan_id) -> web.Response:
    """Retrieve a restricted stock

    This operation retrieves a restricted stock from the plan.

    :param id: ID of restricted stock to retrieve
    :type id: int
    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)


async def restricted_stocks_get_by_planid(request: web.Request, plan_id) -> web.Response:
    """Retrieve restricted stocks

    This operation retrieves a list of all of the restricted stocks in the plan.

    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)
