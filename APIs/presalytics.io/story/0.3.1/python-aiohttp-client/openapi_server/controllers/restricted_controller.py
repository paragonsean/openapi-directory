from typing import List, Dict
from aiohttp import web

from openapi_server.models.collaborator_bulk_update_request import CollaboratorBulkUpdateRequest
from openapi_server.models.permission_type import PermissionType
from openapi_server.models.problem_detail import ProblemDetail
from openapi_server import util


async def collaborators_post(request: web.Request, body) -> web.Response:
    """Collborators: Bulk Update (Admin Only)

    Allows for bulk updates on collaborator metadata.  Restricted to internal admins

    :param body: parameters to identify an update a collaborator across multiple stories
    :type body: dict | bytes

    """
    body = CollaboratorBulkUpdateRequest.from_dict(body)
    return web.Response(status=200)
