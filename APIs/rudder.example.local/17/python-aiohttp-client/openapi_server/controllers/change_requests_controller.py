from typing import List, Dict
from aiohttp import web

from openapi_server.models.accept_change_request200_response import AcceptChangeRequest200Response
from openapi_server.models.accept_change_request_request import AcceptChangeRequestRequest
from openapi_server.models.change_request_details200_response import ChangeRequestDetails200Response
from openapi_server.models.decline_change_request200_response import DeclineChangeRequest200Response
from openapi_server.models.list_change_requests200_response import ListChangeRequests200Response
from openapi_server.models.list_users200_response import ListUsers200Response
from openapi_server.models.remove_validated_user200_response import RemoveValidatedUser200Response
from openapi_server.models.save_workflow_user200_response import SaveWorkflowUser200Response
from openapi_server.models.save_workflow_user_request import SaveWorkflowUserRequest
from openapi_server.models.update_change_request200_response import UpdateChangeRequest200Response
from openapi_server.models.update_change_request_request import UpdateChangeRequestRequest
from openapi_server import util


async def accept_change_request(request: web.Request, change_request_id, body) -> web.Response:
    """Accept a request details

    Accept a change request

    :param change_request_id: 
    :type change_request_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = AcceptChangeRequestRequest.from_dict(body)
    return web.Response(status=200)


async def change_request_details(request: web.Request, change_request_id) -> web.Response:
    """Get a change request details

    Get a change request details

    :param change_request_id: 
    :type change_request_id: int

    """
    return web.Response(status=200)


async def decline_change_request(request: web.Request, change_request_id) -> web.Response:
    """Decline a request details

    Refuse a change request

    :param change_request_id: 
    :type change_request_id: int

    """
    return web.Response(status=200)


async def list_change_requests(request: web.Request, ) -> web.Response:
    """List all change requests

    List all change requests


    """
    return web.Response(status=200)


async def list_users(request: web.Request, ) -> web.Response:
    """List user

    List all validated and unvalidated users


    """
    return web.Response(status=200)


async def remove_validated_user(request: web.Request, username) -> web.Response:
    """Remove an user from validated user list

    The user is again subject to workflow validation

    :param username: Username of an user (unique)
    :type username: str

    """
    return web.Response(status=200)


async def save_workflow_user(request: web.Request, body) -> web.Response:
    """Update validated user list

    Add and remove user from validated users

    :param body: 
    :type body: dict | bytes

    """
    body = SaveWorkflowUserRequest.from_dict(body)
    return web.Response(status=200)


async def update_change_request(request: web.Request, change_request_id, body) -> web.Response:
    """Update a request details

    Update a change request

    :param change_request_id: 
    :type change_request_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateChangeRequestRequest.from_dict(body)
    return web.Response(status=200)
