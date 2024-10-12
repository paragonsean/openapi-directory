from typing import List, Dict
from aiohttp import web

from openapi_server.models.apps_response import AppsResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.user_response import UserResponse
from openapi_server.models.user_update_request import UserUpdateRequest
from openapi_server.models.user_visible_apps_linkages_request import UserVisibleAppsLinkagesRequest
from openapi_server.models.user_visible_apps_linkages_response import UserVisibleAppsLinkagesResponse
from openapi_server.models.users_response import UsersResponse
from openapi_server import util


async def users_delete_instance(request: web.Request, id) -> web.Response:
    """users_delete_instance

    

    :param id: the id of the requested resource
    :type id: str

    """
    return web.Response(status=200)


async def users_get_collection(request: web.Request, filter_roles=None, filter_username=None, filter_visible_apps=None, sort=None, fields_users=None, limit=None, include=None, fields_apps=None, limit_visible_apps=None) -> web.Response:
    """users_get_collection

    

    :param filter_roles: filter by attribute &#39;roles&#39;
    :type filter_roles: List[str]
    :param filter_username: filter by attribute &#39;username&#39;
    :type filter_username: List[str]
    :param filter_visible_apps: filter by id(s) of related &#39;visibleApps&#39;
    :type filter_visible_apps: List[str]
    :param sort: comma-separated list of sort expressions; resources will be sorted as specified
    :type sort: List[str]
    :param fields_users: the fields to include for returned resources of type users
    :type fields_users: List[str]
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


async def users_get_instance(request: web.Request, id, fields_users=None, include=None, fields_apps=None, limit_visible_apps=None) -> web.Response:
    """users_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_users: the fields to include for returned resources of type users
    :type fields_users: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]
    :param limit_visible_apps: maximum number of related visibleApps returned (when they are included)
    :type limit_visible_apps: int

    """
    return web.Response(status=200)


async def users_update_instance(request: web.Request, id, body) -> web.Response:
    """users_update_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param body: User representation
    :type body: dict | bytes

    """
    body = UserUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def users_visible_apps_create_to_many_relationship(request: web.Request, id, body) -> web.Response:
    """users_visible_apps_create_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param body: List of related linkages
    :type body: dict | bytes

    """
    body = UserVisibleAppsLinkagesRequest.from_dict(body)
    return web.Response(status=200)


async def users_visible_apps_delete_to_many_relationship(request: web.Request, id, body) -> web.Response:
    """users_visible_apps_delete_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param body: List of related linkages
    :type body: dict | bytes

    """
    body = UserVisibleAppsLinkagesRequest.from_dict(body)
    return web.Response(status=200)


async def users_visible_apps_get_to_many_related(request: web.Request, id, fields_apps=None, limit=None) -> web.Response:
    """users_visible_apps_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def users_visible_apps_get_to_many_relationship(request: web.Request, id, limit=None) -> web.Response:
    """users_visible_apps_get_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def users_visible_apps_replace_to_many_relationship(request: web.Request, id, body) -> web.Response:
    """users_visible_apps_replace_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param body: List of related linkages
    :type body: dict | bytes

    """
    body = UserVisibleAppsLinkagesRequest.from_dict(body)
    return web.Response(status=200)
