from typing import List, Dict
from aiohttp import web

from openapi_server.models.apps_response import AppsResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.user_invitation_create_request import UserInvitationCreateRequest
from openapi_server.models.user_invitation_response import UserInvitationResponse
from openapi_server.models.user_invitations_response import UserInvitationsResponse
from openapi_server import util


async def user_invitations_create_instance(request: web.Request, body) -> web.Response:
    """user_invitations_create_instance

    

    :param body: UserInvitation representation
    :type body: dict | bytes

    """
    body = UserInvitationCreateRequest.from_dict(body)
    return web.Response(status=200)


async def user_invitations_delete_instance(request: web.Request, id) -> web.Response:
    """user_invitations_delete_instance

    

    :param id: the id of the requested resource
    :type id: str

    """
    return web.Response(status=200)


async def user_invitations_get_collection(request: web.Request, filter_email=None, filter_roles=None, filter_visible_apps=None, sort=None, fields_user_invitations=None, limit=None, include=None, fields_apps=None, limit_visible_apps=None) -> web.Response:
    """user_invitations_get_collection

    

    :param filter_email: filter by attribute &#39;email&#39;
    :type filter_email: List[str]
    :param filter_roles: filter by attribute &#39;roles&#39;
    :type filter_roles: List[str]
    :param filter_visible_apps: filter by id(s) of related &#39;visibleApps&#39;
    :type filter_visible_apps: List[str]
    :param sort: comma-separated list of sort expressions; resources will be sorted as specified
    :type sort: List[str]
    :param fields_user_invitations: the fields to include for returned resources of type userInvitations
    :type fields_user_invitations: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]
    :param limit_visible_apps: maximum number of related visibleApps returned (when they are included)
    :type limit_visible_apps: int

    """
    return web.Response(status=200)


async def user_invitations_get_instance(request: web.Request, id, fields_user_invitations=None, include=None, fields_apps=None, limit_visible_apps=None) -> web.Response:
    """user_invitations_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_user_invitations: the fields to include for returned resources of type userInvitations
    :type fields_user_invitations: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]
    :param limit_visible_apps: maximum number of related visibleApps returned (when they are included)
    :type limit_visible_apps: int

    """
    return web.Response(status=200)


async def user_invitations_visible_apps_get_to_many_related(request: web.Request, id, fields_apps=None, limit=None) -> web.Response:
    """user_invitations_visible_apps_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)
