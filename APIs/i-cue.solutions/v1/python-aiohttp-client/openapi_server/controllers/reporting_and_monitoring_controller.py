from typing import List, Dict
from aiohttp import web

from openapi_server.models.portfolio_model import PortfolioModel
from openapi_server import util


async def report_performance_planning_level_id_get(request: web.Request, planning_level_id, token=None) -> web.Response:
    """Month over month performance per planning level

    Month over month performance per planning level

    :param planning_level_id: 
    :type planning_level_id: str
    :param token: User Authentication Token
    :type token: str

    """
    return web.Response(status=200)


async def report_performance_sku_rationalization_planning_level_id_get(request: web.Request, planning_level_id, token=None) -> web.Response:
    """SKU rationalization report

    SKU rationalization report

    :param planning_level_id: 
    :type planning_level_id: int
    :param token: User Authentication Token
    :type token: str

    """
    return web.Response(status=200)


async def report_planning_level_organization_get(request: web.Request, token=None) -> web.Response:
    """Get list of plannign levels by organization

    Get list of plannign levels by organization

    :param token: User Authentication Token
    :type token: str

    """
    return web.Response(status=200)


async def report_planning_level_user_get(request: web.Request, token=None) -> web.Response:
    """Get list of plannign levels by user

    Get list of plannign levels by user

    :param token: User Authentication Token
    :type token: str

    """
    return web.Response(status=200)


async def report_user_get(request: web.Request, token=None) -> web.Response:
    """Get usage statistics per user

    Get usage statistics per user

    :param token: User Authentication Token
    :type token: str

    """
    return web.Response(status=200)
