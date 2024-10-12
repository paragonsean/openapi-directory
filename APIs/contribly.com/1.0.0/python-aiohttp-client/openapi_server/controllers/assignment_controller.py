from typing import List, Dict
from aiohttp import web

from openapi_server.models.assignment import Assignment
from openapi_server.models.assignment_submission import AssignmentSubmission
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def assignments_get(request: web.Request, owned_by=None, page=None, page_size=None, q=None, url_words=None, open=None, always_open=None, tag=None, name=None) -> web.Response:
    """List assignments

    

    :param owned_by: Restrict results to assignments owned by this user.
    :type owned_by: str
    :param page: Pagination page
    :type page: int
    :param page_size: Pagination page size
    :type page_size: int
    :param q: Restrict results to assignments whose name or description matches this keyword.
    :type q: str
    :param url_words: Select an assignment by urlWords.
    :type url_words: str
    :param open: Select open or closed assignments
    :type open: bool
    :param always_open: Select assignments with no closing date.
    :type always_open: bool
    :param tag: Restrict results to assignments which are tagged with this tag.
    :type tag: str
    :param name: Restrict results to the assignment (or potentially assignments) with this exact name
    :type name: str

    """
    return web.Response(status=200)


async def assignments_id_delete(request: web.Request, id) -> web.Response:
    """Delete this assignment and all of it&#39;s contributions

    

    :param id: Id of the assignment to return
    :type id: str

    """
    return web.Response(status=200)


async def assignments_id_get(request: web.Request, id) -> web.Response:
    """Get a single assigment by id

    

    :param id: Id of the assignment to return
    :type id: str

    """
    return web.Response(status=200)


async def assignments_post(request: web.Request, body) -> web.Response:
    """Create a new assignment

    

    :param body: Assignment object to be created
    :type body: dict | bytes

    """
    body = AssignmentSubmission.from_dict(body)
    return web.Response(status=200)
