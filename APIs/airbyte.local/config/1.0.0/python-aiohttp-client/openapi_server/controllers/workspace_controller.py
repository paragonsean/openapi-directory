from typing import List, Dict
from aiohttp import web

from openapi_server.models.connection_id_request_body import ConnectionIdRequestBody
from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_server.models.slug_request_body import SlugRequestBody
from openapi_server.models.workspace_create import WorkspaceCreate
from openapi_server.models.workspace_give_feedback import WorkspaceGiveFeedback
from openapi_server.models.workspace_id_request_body import WorkspaceIdRequestBody
from openapi_server.models.workspace_read import WorkspaceRead
from openapi_server.models.workspace_read_list import WorkspaceReadList
from openapi_server.models.workspace_update import WorkspaceUpdate
from openapi_server.models.workspace_update_name import WorkspaceUpdateName
from openapi_server import util


async def create_workspace(request: web.Request, body) -> web.Response:
    """Creates a workspace

    

    :param body: 
    :type body: dict | bytes

    """
    body = WorkspaceCreate.from_dict(body)
    return web.Response(status=200)


async def delete_workspace(request: web.Request, body) -> web.Response:
    """Deletes a workspace

    

    :param body: 
    :type body: dict | bytes

    """
    body = WorkspaceIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def get_workspace(request: web.Request, body) -> web.Response:
    """Find workspace by ID

    

    :param body: 
    :type body: dict | bytes

    """
    body = WorkspaceIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def get_workspace_by_connection_id(request: web.Request, body) -> web.Response:
    """Find workspace by connection id

    

    :param body: 
    :type body: dict | bytes

    """
    body = ConnectionIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def get_workspace_by_slug(request: web.Request, body) -> web.Response:
    """Find workspace by slug

    

    :param body: 
    :type body: dict | bytes

    """
    body = SlugRequestBody.from_dict(body)
    return web.Response(status=200)


async def list_workspaces(request: web.Request, ) -> web.Response:
    """List all workspaces registered in the current Airbyte deployment

    


    """
    return web.Response(status=200)


async def update_workspace(request: web.Request, body) -> web.Response:
    """Update workspace state

    

    :param body: 
    :type body: dict | bytes

    """
    body = WorkspaceUpdate.from_dict(body)
    return web.Response(status=200)


async def update_workspace_feedback(request: web.Request, body) -> web.Response:
    """Update workspace feedback state

    

    :param body: 
    :type body: dict | bytes

    """
    body = WorkspaceGiveFeedback.from_dict(body)
    return web.Response(status=200)


async def update_workspace_name(request: web.Request, body) -> web.Response:
    """Update workspace name

    

    :param body: 
    :type body: dict | bytes

    """
    body = WorkspaceUpdateName.from_dict(body)
    return web.Response(status=200)
