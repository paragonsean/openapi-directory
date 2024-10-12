from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_workspace_request import AddWorkspaceRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_all_workspaces_response import GetAllWorkspacesResponse
from openapi_server import util


async def add_workspace(request: web.Request, body) -> web.Response:
    """Claim a Mailscript workspace

    An attendant address will be created as well

    :param body: request body
    :type body: dict | bytes

    """
    body = AddWorkspaceRequest.from_dict(body)
    return web.Response(status=200)


async def get_all_workspaces(request: web.Request, ) -> web.Response:
    """Get all workspaces you have access to

    


    """
    return web.Response(status=200)
