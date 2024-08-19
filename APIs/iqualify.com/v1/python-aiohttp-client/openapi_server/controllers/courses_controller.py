from typing import List, Dict
from aiohttp import web

from openapi_server.models.activation_response import ActivationResponse
from openapi_server.models.course_meta_response import CourseMetaResponse
from openapi_server.models.course_response import CourseResponse
from openapi_server.models.courses_root_content_id_permissions_user_email_post201_response import CoursesRootContentIdPermissionsUserEmailPost201Response
from openapi_server.models.error import Error
from openapi_server.models.permission_to_be_granted_to_the_user import PermissionToBeGrantedToTheUser
from openapi_server.models.user_permission import UserPermission
from openapi_server import util


async def courses_content_id_activations_get(request: web.Request, content_id) -> web.Response:
    """Find activations for a contentId

    Responds with all activations for the contentId provided.

    :param content_id: The content Id
    :type content_id: str

    """
    return web.Response(status=200)


async def courses_content_id_get(request: web.Request, content_id) -> web.Response:
    """Find course by contentId

    Responds with a course matching the contentId.

    :param content_id: The content Id
    :type content_id: str

    """
    return web.Response(status=200)


async def courses_content_id_permissions_get(request: web.Request, content_id) -> web.Response:
    """Find users who have access to the contentId provided

    Responds with users who have access to a specific course by contentId.

    :param content_id: The content Id
    :type content_id: str

    """
    return web.Response(status=200)


async def courses_get(request: web.Request, ) -> web.Response:
    """Find courses

    Responds with all courses (draft and published.)


    """
    return web.Response(status=200)


async def courses_root_content_id_permissions_user_email_post(request: web.Request, root_content_id, user_email, body) -> web.Response:
    """Update course access

    Provide a user with access to a specific course by rootContentId.

    :param root_content_id: The content Id
    :type root_content_id: str
    :param user_email: The user email
    :type user_email: str
    :param body: 
    :type body: dict | bytes

    """
    body = PermissionToBeGrantedToTheUser.from_dict(body)
    return web.Response(status=200)
