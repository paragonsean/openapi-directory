from typing import List, Dict
from aiohttp import web

from openapi_server.models.district_response import DistrictResponse
from openapi_server.models.not_found import NotFound
from openapi_server.models.school_response import SchoolResponse
from openapi_server.models.sections_response import SectionsResponse
from openapi_server.models.student_contacts_for_student_response import StudentContactsForStudentResponse
from openapi_server.models.student_response import StudentResponse
from openapi_server.models.students_response import StudentsResponse
from openapi_server.models.teachers_response import TeachersResponse
from openapi_server import util


async def get_contacts_for_student(request: web.Request, id, limit=None) -> web.Response:
    """get_contacts_for_student

    Returns the contacts for a student

    :param id: 
    :type id: str
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def get_district_for_student(request: web.Request, id) -> web.Response:
    """get_district_for_student

    Returns the district for a student

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_school_for_student(request: web.Request, id) -> web.Response:
    """get_school_for_student

    Returns the primary school for a student

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_sections_for_student(request: web.Request, id, limit=None, starting_after=None, ending_before=None) -> web.Response:
    """get_sections_for_student

    Returns the sections for a student

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


async def get_student(request: web.Request, id, include=None) -> web.Response:
    """get_student

    Returns a specific student

    :param id: 
    :type id: str
    :param include: 
    :type include: str

    """
    return web.Response(status=200)


async def get_students(request: web.Request, limit=None, starting_after=None, ending_before=None, where=None) -> web.Response:
    """get_students

    Returns a list of students

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


async def get_teachers_for_student(request: web.Request, id, limit=None, starting_after=None, ending_before=None) -> web.Response:
    """get_teachers_for_student

    Returns the teachers for a student

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
