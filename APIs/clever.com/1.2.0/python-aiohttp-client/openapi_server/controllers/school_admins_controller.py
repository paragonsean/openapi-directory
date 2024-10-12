from typing import List, Dict
from aiohttp import web

from openapi_server.models.not_found import NotFound
from openapi_server.models.school_admin_response import SchoolAdminResponse
from openapi_server.models.school_admins_response import SchoolAdminsResponse
from openapi_server.models.schools_response import SchoolsResponse
from openapi_server import util


async def get_school_admin(request: web.Request, id, include=None) -> web.Response:
    """get_school_admin

    Returns a specific school admin

    :param id: 
    :type id: str
    :param include: 
    :type include: str

    """
    return web.Response(status=200)


async def get_school_admins(request: web.Request, limit=None, starting_after=None, ending_before=None, where=None) -> web.Response:
    """get_school_admins

    Returns a list of school admins

    :param limit: 
    :type limit: int
    :param starting_after: 
    :type starting_after: str
    :param ending_before: 
    :type ending_before: str
    :param where: 
    :type where: str

    """
    return web.Response(status=200)


async def get_schools_for_school_admin(request: web.Request, id, limit=None, starting_after=None, ending_before=None) -> web.Response:
    """get_schools_for_school_admin

    Returns the schools for a school admin

    :param id: 
    :type id: str
    :param limit: 
    :type limit: int
    :param starting_after: 
    :type starting_after: str
    :param ending_before: 
    :type ending_before: str

    """
    return web.Response(status=200)
