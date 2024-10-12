from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_workflow_request import AddWorkflowRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_all_workflows_response import GetAllWorkflowsResponse
from openapi_server.models.set_workflow_request import SetWorkflowRequest
from openapi_server import util


async def add_workflow(request: web.Request, body) -> web.Response:
    """Setup workflow

    

    :param body: Workflow body
    :type body: dict | bytes

    """
    body = AddWorkflowRequest.from_dict(body)
    return web.Response(status=200)


async def delete_workflow(request: web.Request, workflow) -> web.Response:
    """Delete a workflow

    

    :param workflow: ID of the workflow
    :type workflow: str

    """
    return web.Response(status=200)


async def get_all_workflows(request: web.Request, ) -> web.Response:
    """Get all workflows you have access to

    


    """
    return web.Response(status=200)


async def set_workflow(request: web.Request, body) -> web.Response:
    """Set a property on a workflow

    

    :param body: Set Workflow body
    :type body: dict | bytes

    """
    body = SetWorkflowRequest.from_dict(body)
    return web.Response(status=200)


async def update_workflow(request: web.Request, workflow, body) -> web.Response:
    """Update an workflow

    

    :param workflow: ID of the workflow
    :type workflow: str
    :param body: Workflow body
    :type body: dict | bytes

    """
    body = AddWorkflowRequest.from_dict(body)
    return web.Response(status=200)
