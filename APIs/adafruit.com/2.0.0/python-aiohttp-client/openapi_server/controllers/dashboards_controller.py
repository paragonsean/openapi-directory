from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_dashboard_request import CreateDashboardRequest
from openapi_server.models.dashboard import Dashboard
from openapi_server import util


async def all_dashboards(request: web.Request, username) -> web.Response:
    """All dashboards for current user

    The Dashboards endpoint returns information about the user&#39;s dashboards. 

    :param username: a valid username string
    :type username: str

    """
    return web.Response(status=200)


async def create_dashboard(request: web.Request, username, dashboard) -> web.Response:
    """Create a new Dashboard

    

    :param username: a valid username string
    :type username: str
    :param dashboard: 
    :type dashboard: dict | bytes

    """
    dashboard = CreateDashboardRequest.from_dict(dashboard)
    return web.Response(status=200)


async def destroy_dashboard(request: web.Request, username, id) -> web.Response:
    """Delete an existing Dashboard

    

    :param username: a valid username string
    :type username: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_dashboard(request: web.Request, username, id) -> web.Response:
    """Returns Dashboard based on ID

    

    :param username: a valid username string
    :type username: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def replace_dashboard(request: web.Request, username, id, dashboard) -> web.Response:
    """Replace an existing Dashboard

    

    :param username: a valid username string
    :type username: str
    :param id: 
    :type id: str
    :param dashboard: 
    :type dashboard: dict | bytes

    """
    dashboard = CreateDashboardRequest.from_dict(dashboard)
    return web.Response(status=200)


async def update_dashboard(request: web.Request, username, id, dashboard) -> web.Response:
    """Update properties of an existing Dashboard

    

    :param username: a valid username string
    :type username: str
    :param id: 
    :type id: str
    :param dashboard: 
    :type dashboard: dict | bytes

    """
    dashboard = CreateDashboardRequest.from_dict(dashboard)
    return web.Response(status=200)
