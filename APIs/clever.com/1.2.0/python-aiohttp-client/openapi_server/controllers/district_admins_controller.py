from typing import List, Dict
from aiohttp import web

from openapi_server.models.district_admin_response import DistrictAdminResponse
from openapi_server.models.district_admins_response import DistrictAdminsResponse
from openapi_server.models.not_found import NotFound
from openapi_server import util


async def get_district_admin(request: web.Request, id) -> web.Response:
    """get_district_admin

    Returns a specific district admin

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_district_admins(request: web.Request, starting_after=None, ending_before=None, show_links=None) -> web.Response:
    """get_district_admins

    Returns a list of district admins

    :param starting_after: 
    :type starting_after: str
    :param ending_before: 
    :type ending_before: str
    :param show_links: 
    :type show_links: str

    """
    return web.Response(status=200)
