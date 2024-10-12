from typing import List, Dict
from aiohttp import web

from openapi_server.models.portfolio_account_model import PortfolioAccountModel
from openapi_server.models.portfolio_accounts_model import PortfolioAccountsModel
from openapi_server import util


async def portfolio_accounts_get_by_id_planid(request: web.Request, id, plan_id) -> web.Response:
    """Retrieve a portfolio account

    This operation retrieves a portfolio account from the plan.

    :param id: ID of portfolio account to retrieve
    :type id: int
    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)


async def portfolio_accounts_get_by_planid(request: web.Request, plan_id) -> web.Response:
    """Retrieve portfolio accounts

    This operation retrieves a list of all of the portfolio accounts in the plan.

    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)
