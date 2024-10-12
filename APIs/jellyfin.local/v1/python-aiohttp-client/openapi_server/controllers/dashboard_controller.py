from typing import List, Dict
from aiohttp import web

from openapi_server.models.configuration_page_info import ConfigurationPageInfo
from openapi_server.models.configuration_page_type import ConfigurationPageType
from openapi_server.models.problem_details import ProblemDetails
from openapi_server import util


async def get_configuration_pages(request: web.Request, enable_in_main_menu=None, page_type=None) -> web.Response:
    """Gets the configuration pages.

    

    :param enable_in_main_menu: Whether to enable in the main menu.
    :type enable_in_main_menu: bool
    :param page_type: The Jellyfin.Api.Models.ConfigurationPageInfo.
    :type page_type: dict | bytes

    """
    page_type = .from_dict(page_type)
    return web.Response(status=200)


async def get_dashboard_configuration_page(request: web.Request, name=None) -> web.Response:
    """Gets a dashboard configuration page.

    

    :param name: The name of the page.
    :type name: str

    """
    return web.Response(status=200)
