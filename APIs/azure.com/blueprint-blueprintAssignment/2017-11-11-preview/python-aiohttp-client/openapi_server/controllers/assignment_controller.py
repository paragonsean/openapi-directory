from typing import List, Dict
from aiohttp import web

from openapi_server.models.assignment import Assignment
from openapi_server.models.assignment_list import AssignmentList
from openapi_server import util


async def assignments_create_or_update(request: web.Request, api_version, subscription_id, assignment_name, assignment) -> web.Response:
    """assignments_create_or_update

    Create or update a Blueprint assignment.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: azure subscriptionId, which we assign the blueprint to.
    :type subscription_id: str
    :param assignment_name: name of the assignment.
    :type assignment_name: str
    :param assignment: assignment object to save.
    :type assignment: dict | bytes

    """
    assignment = Assignment.from_dict(assignment)
    return web.Response(status=200)


async def assignments_delete(request: web.Request, api_version, subscription_id, assignment_name) -> web.Response:
    """assignments_delete

    Delete a Blueprint assignment.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: azure subscriptionId, which we assign the blueprint to.
    :type subscription_id: str
    :param assignment_name: name of the assignment.
    :type assignment_name: str

    """
    return web.Response(status=200)


async def assignments_get(request: web.Request, api_version, subscription_id, assignment_name) -> web.Response:
    """assignments_get

    Get a Blueprint assignment.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: azure subscriptionId, which we assign the blueprint to.
    :type subscription_id: str
    :param assignment_name: name of the assignment.
    :type assignment_name: str

    """
    return web.Response(status=200)


async def assignments_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """assignments_list

    List Blueprint assignments within a subscription.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: azure subscriptionId, which we assign the blueprint to.
    :type subscription_id: str

    """
    return web.Response(status=200)
