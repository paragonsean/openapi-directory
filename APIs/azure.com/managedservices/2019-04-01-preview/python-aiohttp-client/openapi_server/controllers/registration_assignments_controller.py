from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.registration_assignment import RegistrationAssignment
from openapi_server.models.registration_assignment_list import RegistrationAssignmentList
from openapi_server import util


async def registration_assignments_create_or_update(request: web.Request, scope, registration_assignment_id, api_version, request_body) -> web.Response:
    """registration_assignments_create_or_update

    Creates or updates a registration assignment.

    :param scope: Scope of the resource.
    :type scope: str
    :param registration_assignment_id: Guid of the registration assignment.
    :type registration_assignment_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param request_body: The parameters required to create new registration assignment.
    :type request_body: dict | bytes

    """
    request_body = RegistrationAssignment.from_dict(request_body)
    return web.Response(status=200)


async def registration_assignments_delete(request: web.Request, scope, registration_assignment_id, api_version) -> web.Response:
    """registration_assignments_delete

    Deletes the specified registration assignment.

    :param scope: Scope of the resource.
    :type scope: str
    :param registration_assignment_id: Guid of the registration assignment.
    :type registration_assignment_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def registration_assignments_get(request: web.Request, scope, registration_assignment_id, api_version, expand_registration_definition=None) -> web.Response:
    """registration_assignments_get

    Gets the details of specified registration assignment.

    :param scope: Scope of the resource.
    :type scope: str
    :param registration_assignment_id: Guid of the registration assignment.
    :type registration_assignment_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param expand_registration_definition: Tells whether to return registration definition details also along with registration assignment details.
    :type expand_registration_definition: bool

    """
    return web.Response(status=200)


async def registration_assignments_list(request: web.Request, scope, api_version, expand_registration_definition=None) -> web.Response:
    """registration_assignments_list

    Gets a list of the registration assignments.

    :param scope: Scope of the resource.
    :type scope: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param expand_registration_definition: Tells whether to return registration definition details also along with registration assignment details.
    :type expand_registration_definition: bool

    """
    return web.Response(status=200)
