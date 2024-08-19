from typing import List, Dict
from aiohttp import web

from openapi_server.models.district_response import DistrictResponse
from openapi_server.models.not_found import NotFound
from openapi_server.models.school_response import SchoolResponse
from openapi_server.models.section_response import SectionResponse
from openapi_server.models.sections_response import SectionsResponse
from openapi_server.models.students_response import StudentsResponse
from openapi_server.models.teacher_response import TeacherResponse
from openapi_server.models.teachers_response import TeachersResponse
from openapi_server import util


async def get_district_for_section(request: web.Request, id) -> web.Response:
    """get_district_for_section

    Returns the district for a section

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_school_for_section(request: web.Request, id) -> web.Response:
    """get_school_for_section

    Returns the school for a section

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_section(request: web.Request, id) -> web.Response:
    """get_section

    Returns a specific section

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_sections(request: web.Request, limit=None, starting_after=None, ending_before=None, where=None) -> web.Response:
    """get_sections

    Returns a list of sections

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


async def get_students_for_section(request: web.Request, id, limit=None, starting_after=None, ending_before=None) -> web.Response:
    """get_students_for_section

    Returns the students for a section

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


async def get_teacher_for_section(request: web.Request, id) -> web.Response:
    """get_teacher_for_section

    Returns the primary teacher for a section

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_teachers_for_section(request: web.Request, id, limit=None, starting_after=None, ending_before=None) -> web.Response:
    """get_teachers_for_section

    Returns the teachers for a section

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
