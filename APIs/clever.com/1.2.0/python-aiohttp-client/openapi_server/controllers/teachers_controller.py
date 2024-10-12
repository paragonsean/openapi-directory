from typing import List, Dict
from aiohttp import web

from openapi_server.models.district_response import DistrictResponse
from openapi_server.models.grade_levels_response import GradeLevelsResponse
from openapi_server.models.not_found import NotFound
from openapi_server.models.school_response import SchoolResponse
from openapi_server.models.sections_response import SectionsResponse
from openapi_server.models.students_response import StudentsResponse
from openapi_server.models.teacher_response import TeacherResponse
from openapi_server.models.teachers_response import TeachersResponse
from openapi_server import util


async def get_district_for_teacher(request: web.Request, id) -> web.Response:
    """get_district_for_teacher

    Returns the district for a teacher

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_grade_levels_for_teacher(request: web.Request, id) -> web.Response:
    """get_grade_levels_for_teacher

    Returns the grade levels for sections a teacher teaches

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_school_for_teacher(request: web.Request, id) -> web.Response:
    """get_school_for_teacher

    Retrieves school info for a teacher.

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_sections_for_teacher(request: web.Request, id, limit=None, starting_after=None, ending_before=None) -> web.Response:
    """get_sections_for_teacher

    Returns the sections for a teacher

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


async def get_students_for_teacher(request: web.Request, id, limit=None, starting_after=None, ending_before=None) -> web.Response:
    """get_students_for_teacher

    Returns the students for a teacher

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


async def get_teacher(request: web.Request, id, include=None) -> web.Response:
    """get_teacher

    Returns a specific teacher

    :param id: 
    :type id: str
    :param include: 
    :type include: str

    """
    return web.Response(status=200)


async def get_teachers(request: web.Request, limit=None, starting_after=None, ending_before=None, where=None) -> web.Response:
    """get_teachers

    Returns a list of teachers

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
