from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_reimbursement_request import CreateReimbursementRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.policy_update_input import PolicyUpdateInput
from openapi_server import util


async def create_reimbursement(request: web.Request, project_id, body) -> web.Response:
    """Create Reimbursement

    Create a new Reimbursement policy

    :param project_id: 
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateReimbursementRequest.from_dict(body)
    return web.Response(status=200)


async def update_reimbursement(request: web.Request, project_id, body) -> web.Response:
    """Update Reimbursement

    Update an existing Reimbursement policy

    :param project_id: 
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PolicyUpdateInput.from_dict(body)
    return web.Response(status=200)
