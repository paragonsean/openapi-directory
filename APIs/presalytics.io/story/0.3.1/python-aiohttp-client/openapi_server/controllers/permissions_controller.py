from typing import List, Dict
from aiohttp import web

from openapi_server.models.permission_type import PermissionType
from openapi_server.models.problem_detail import ProblemDetail
from openapi_server import util


async def story_id_collaborators_userid_permissiontype_get(request: web.Request, id, story_collaborator_userid, permissiontype) -> web.Response:
    """Permissions: Story Authorization for a User

    Check whether user have certain types of permissions.  Use http status codes to understand if permission is granted - 204 &#x3D; Granted, 403 &#x3D; Forbidden

    :param id: the id from the story object
    :type id: str
    :type id: str
    :param story_collaborator_userid: The presalytics userid (NOT the Id of the story_collaborator object)
    :type story_collaborator_userid: str
    :type story_collaborator_userid: str
    :param permissiontype: the type of permission requested.  can be a permission_type object name (e.g., owner, editor, create, viewer, admin) or a permission type field (e.g., can_edit, can_view, can_add_collaborators, can_delete)
    :type permissiontype: str

    """
    return web.Response(status=200)


async def story_permission_types_get(request: web.Request, ) -> web.Response:
    """Permissions: List Permission Types

    Returns a list of possible user permission types


    """
    return web.Response(status=200)
