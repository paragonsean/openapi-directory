from typing import List, Dict
from aiohttp import web

from openapi_server.models.forecast_performance_request import ForecastPerformanceRequest
from openapi_server.models.portfolio_abc_model import PortfolioAbcModel
from openapi_server.models.portfolio_model import PortfolioModel
from openapi_server.models.portfolio_request import PortfolioRequest
from openapi_server.models.portfolio_xyz_model import PortfolioXyzModel
from openapi_server.models.rewind_response import RewindResponse
from openapi_server import util


async def portfolio_abc_post(request: web.Request, token=None, body=None) -> web.Response:
    """ABC Analysis

    Calculate and retrieve results of ABC (pareto analysis) per timeseries and planning level.

    :param token: User Authentication Token
    :type token: str
    :param body: 
    :type body: dict | bytes

    """
    body = PortfolioRequest.from_dict(body)
    return web.Response(status=200)


async def portfolio_file_to_portfolio_post(request: web.Request, file, token=None) -> web.Response:
    """ABCxyz Analysis

    Calculate and retrieve results of ABC (pareto analysis) and xyz (Coefficient of variation) per timeseries and planning level. This analysis is a powerful means to estbalish a proper planning cadence, best accuracy messures and optimal hyperparameters for the organization. It provides a balanced and actionable overview of the entire product portfolio.

    :param file: 
    :type file: str
    :param token: User Authentication Token
    :type token: str

    """
    return web.Response(status=200)


async def portfolio_forecast_performance_rewind_post(request: web.Request, token=None, body=None) -> web.Response:
    """Planning level rewind to calculate and measure performance potential (internal versus iCUE).

    Planning level rewind to calculate and measure performance potential (internal versus iCUE).

    :param token: User Authentication Token
    :type token: str
    :param body: 
    :type body: dict | bytes

    """
    body = ForecastPerformanceRequest.from_dict(body)
    return web.Response(status=200)


async def portfolio_post(request: web.Request, token=None, body=None) -> web.Response:
    """ABCxyz Analysis

    Calculate and retrieve results of ABC (pareto analysis) and xyz (Coefficient of variation) per timeseries and planning level. This analysis is a powerful means to estbalish a proper planning cadence, best accuracy messures and optimal hyperparameters for the organization. It provides a balanced and actionable overview of the entire product portfolio.

    :param token: User Authentication Token
    :type token: str
    :param body: 
    :type body: dict | bytes

    """
    body = PortfolioRequest.from_dict(body)
    return web.Response(status=200)


async def portfolio_xyz_post(request: web.Request, token=None, body=None) -> web.Response:
    """xyz Analysis

    Calculate and retrieve results of xyz (Coefficient of variation) per timeseries and planning level.

    :param token: User Authentication Token
    :type token: str
    :param body: 
    :type body: dict | bytes

    """
    body = PortfolioRequest.from_dict(body)
    return web.Response(status=200)
