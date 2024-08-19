from typing import List, Dict
from aiohttp import web

from openapi_server.models.district_admins_response import DistrictAdminsResponse
from openapi_server.models.district_response import DistrictResponse
from openapi_server.models.district_status_responses import DistrictStatusResponses
from openapi_server.models.districts_response import DistrictsResponse
from openapi_server.models.not_found import NotFound
from openapi_server.models.schools_response import SchoolsResponse
from openapi_server.models.sections_response import SectionsResponse
from openapi_server.models.students_response import StudentsResponse
from openapi_server.models.teachers_response import TeachersResponse
from openapi_server import util


async def get_admins_for_district(request: web.Request, id) -> web.Response:
    """get_admins_for_district

    Returns the admins for a district

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_district(request: web.Request, id, include=None) -> web.Response:
    """get_district

    Returns a specific district

    :param id: 
    :type id: str
    :param include: 
    :type include: str

    """
    return web.Response(status=200)


async def get_district_status(request: web.Request, id) -> web.Response:
    """get_district_status

    Returns the status of the district

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_districts(request: web.Request, ) -> web.Response:
    """get_districts

    Returns a list of districts. In practice this will only return the one district associated with the bearer token


    """
    return web.Response(status=200)


async def get_schools_for_district(request: web.Request, id, limit=None, starting_after=None, ending_before=None, where=None) -> web.Response:
    """get_schools_for_district

    Returns the schools for a district

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


async def get_sections_for_district(request: web.Request, id, limit=None, starting_after=None, ending_before=None, where=None) -> web.Response:
    """get_sections_for_district

    Returns the sections for a district

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


async def get_students_for_district(request: web.Request, id, limit=None, starting_after=None, ending_before=None, where=None) -> web.Response:
    """get_students_for_district

    Returns the students for a district

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


async def get_teachers_for_district(request: web.Request, id, limit=None, starting_after=None, ending_before=None, where=None) -> web.Response:
    """get_teachers_for_district

    Returns the teachers for a district

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
