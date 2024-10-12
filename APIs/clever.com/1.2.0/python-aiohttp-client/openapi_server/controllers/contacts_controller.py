from typing import List, Dict
from aiohttp import web

from openapi_server.models.district_response import DistrictResponse
from openapi_server.models.not_found import NotFound
from openapi_server.models.student_contact_response import StudentContactResponse
from openapi_server.models.student_contacts_response import StudentContactsResponse
from openapi_server.models.student_response import StudentResponse
from openapi_server import util


async def get_contact(request: web.Request, id) -> web.Response:
    """get_contact

    Returns a specific student contact

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_contacts(request: web.Request, limit=None, starting_after=None, ending_before=None) -> web.Response:
    """get_contacts

    Returns a list of student contacts

    :param limit: 
    :type limit: int
    :param starting_after: 
    :type starting_after: str
    :param ending_before: 
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_district_for_student_contact(request: web.Request, id) -> web.Response:
    """get_district_for_student_contact

    Returns the district for a student contact

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_student_for_contact(request: web.Request, id) -> web.Response:
    """get_student_for_contact

    Returns the student for a student contact

    :param id: 
    :type id: str

    """
    return web.Response(status=200)
