from typing import List, Dict
from aiohttp import web

from openapi_server.models.district_response import DistrictResponse
from openapi_server.models.not_found import NotFound
from openapi_server.models.school_response import SchoolResponse
from openapi_server.models.schools_response import SchoolsResponse
from openapi_server.models.sections_response import SectionsResponse
from openapi_server.models.students_response import StudentsResponse
from openapi_server.models.teachers_response import TeachersResponse
from openapi_server import util


async def get_district_for_school(request: web.Request, id) -> web.Response:
    """get_district_for_school

    Returns the district for a school

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_school(request: web.Request, id) -> web.Response:
    """get_school

    Returns a specific school

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_schools(request: web.Request, limit=None, starting_after=None, ending_before=None, where=None) -> web.Response:
    """get_schools

    Returns a list of schools

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


async def get_sections_for_school(request: web.Request, id, limit=None, starting_after=None, ending_before=None, where=None) -> web.Response:
    """get_sections_for_school

    Returns the sections for a school

    :param id: 
    :type id: str
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


async def get_students_for_school(request: web.Request, id, limit=None, starting_after=None, ending_before=None, where=None) -> web.Response:
    """get_students_for_school

    Returns the students for a school

    :param id: 
    :type id: str
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


async def get_teachers_for_school(request: web.Request, id, limit=None, starting_after=None, ending_before=None, where=None) -> web.Response:
    """get_teachers_for_school

    Returns the teachers for a school

    :param id: 
    :type id: str
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
