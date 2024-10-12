from typing import List, Dict
from aiohttp import web

from openapi_server.models.portfolio import Portfolio
from openapi_server import util


async def get_portfolio(request: web.Request, portfolio_id, user_id) -> web.Response:
    """Get a specific portfolio

    

    :param portfolio_id: The ID of the portfolio.
    :type portfolio_id: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def get_portfolio_alt1(request: web.Request, portfolio_id) -> web.Response:
    """Get a specific portfolio

    

    :param portfolio_id: The ID of the portfolio.
    :type portfolio_id: 

    """
    return web.Response(status=200)


async def get_portfolios(request: web.Request, user_id, direction=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all the portfolios that belong to a user

    

    :param user_id: The ID of the user.
    :type user_id: 
    :param direction: The sort direction of the results.
    :type direction: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param query: The search query to use to filter the results.
    :type query: str
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)


async def get_portfolios_alt1(request: web.Request, direction=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all the portfolios that belong to a user

    

    :param direction: The sort direction of the results.
    :type direction: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param query: The search query to use to filter the results.
    :type query: str
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)
