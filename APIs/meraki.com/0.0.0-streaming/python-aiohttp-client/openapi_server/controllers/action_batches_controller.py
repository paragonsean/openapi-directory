from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_organization_action_batch_request import CreateOrganizationActionBatchRequest
from openapi_server.models.update_organization_action_batch_request import UpdateOrganizationActionBatchRequest
from openapi_server import util


async def create_organization_action_batch(request: web.Request, organization_id, body) -> web.Response:
    """Create an action batch

    Create an action batch

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationActionBatchRequest.from_dict(body)
    return web.Response(status=200)


async def delete_organization_action_batch(request: web.Request, organization_id, action_batch_id) -> web.Response:
    """Delete an action batch

    Delete an action batch

    :param organization_id: 
    :type organization_id: str
    :param action_batch_id: 
    :type action_batch_id: str

    """
    return web.Response(status=200)


async def get_organization_action_batches(request: web.Request, organization_id, status=None) -> web.Response:
    """Return the list of action batches in the organization

    Return the list of action batches in the organization

    :param organization_id: 
    :type organization_id: str
    :param status: Filter batches by status. Valid types are pending, completed, and failed.
    :type status: str

    """
    return web.Response(status=200)


async def update_organization_action_batch(request: web.Request, organization_id, action_batch_id, body=None) -> web.Response:
    """Update an action batch

    Update an action batch

    :param organization_id: 
    :type organization_id: str
    :param action_batch_id: 
    :type action_batch_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationActionBatchRequest.from_dict(body)
    return web.Response(status=200)
