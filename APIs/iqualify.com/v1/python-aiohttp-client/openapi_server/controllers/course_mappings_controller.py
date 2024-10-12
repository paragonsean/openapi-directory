from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server import util


async def course_mappings_externalcourse_external_course_id_get(request: web.Request, external_course_id) -> web.Response:
    """Find course mappings by externalCourseId

    Responds with course mapping details by externalCourseId.

    :param external_course_id: external course&#39;s id
    :type external_course_id: str

    """
    return web.Response(status=200)


async def course_mappings_get(request: web.Request, ) -> web.Response:
    """Find course mappings

    Returns all course mappings for course offerings.


    """
    return web.Response(status=200)


async def course_mappings_offering_id_external_course_id_delete(request: web.Request, offering_id, external_course_id) -> web.Response:
    """Remove course mapping

    Removes the course mapping between the offering and the externalCourseId.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param external_course_id: external course&#39;s id
    :type external_course_id: str

    """
    return web.Response(status=200)


async def course_mappings_offering_id_external_course_id_put(request: web.Request, offering_id, external_course_id) -> web.Response:
    """Add course mapping

    Creates a mapping between the offering and the externalCourseId.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param external_course_id: external course&#39;s id
    :type external_course_id: str

    """
    return web.Response(status=200)


async def course_mappings_offering_id_get(request: web.Request, offering_id) -> web.Response:
    """Find course mappings by offeringId

    Responds with course mapping details by offeringId.

    :param offering_id: offering&#39;s id
    :type offering_id: str

    """
    return web.Response(status=200)
