from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.permission import Permission
from openapi_server.models.tag import Tag
from openapi_server import util


async def delete_permission(request: web.Request, permission_id, authorization, api_version) -> web.Response:
    """Deletes the permission object

    Deletes the permission object from the application

    :param permission_id: The permission unique identifier. E.g PERM001
    :type permission_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_permission_tag_0(request: web.Request, permission_id, tag_id, authorization, api_version) -> web.Response:
    """Delete Permission tag

    Deletes a tag from the Permission

    :param permission_id: The permission unique identifier. E.g PERM001
    :type permission_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_permission_tags_0(request: web.Request, authorization, api_version) -> web.Response:
    """Get all Permission tags

    Get all tags from all Permissions

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_permissions_with_tag_0(request: web.Request, tag_id, authorization, api_version) -> web.Response:
    """Get links to tagged Permissions

    Gets the Permissions with the specified tag

    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_permission(request: web.Request, permission_id, authorization, api_version) -> web.Response:
    """Gets the permission object

    Gets the permission object for application

    :param permission_id: The permission unique identifier. E.g PERM001
    :type permission_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_permissions(request: web.Request, authorization, api_version) -> web.Response:
    """Gets all permission objects

    Gets all permission objects for application

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tag_from_permission_0(request: web.Request, permission_id, tag_id, authorization, api_version) -> web.Response:
    """Get Permission tag

    Gets a tag from the Permission

    :param permission_id: The permission unique identifier. E.g PERM001
    :type permission_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tags_from_permission_0(request: web.Request, permission_id, authorization, api_version) -> web.Response:
    """Get tags from Permission

    Gets all tags from the Permission

    :param permission_id: The permission unique identifier. E.g PERM001
    :type permission_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_user_permissions(request: web.Request, user_id, authorization, api_version) -> web.Response:
    """Gets the user permissions

    Gets the user permission instances

    :param user_id: The user unique identifier. E.g USER001
    :type user_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_users_from_permission(request: web.Request, permission_id, authorization, api_version) -> web.Response:
    """Gets the users with the specified permission

    Gets the users with the specified permission

    :param permission_id: The permission unique identifier. E.g PERM001
    :type permission_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def patch_permission(request: web.Request, permission_id, authorization, api_version) -> web.Response:
    """Patch permission object

    Patch the permission object at the specified resource location

    :param permission_id: The permission unique identifier. E.g PERM001
    :type permission_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def post_permission(request: web.Request, authorization, api_version) -> web.Response:
    """Post permisson object

    Post the new permission object into the application

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_permission(request: web.Request, permission_id, authorization, api_version) -> web.Response:
    """Puts permisson object

    Puts the permission object into the specified resource location

    :param permission_id: The permission unique identifier. E.g PERM001
    :type permission_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_permission_tag_0(request: web.Request, permission_id, tag_id, authorization, api_version) -> web.Response:
    """Insert Permission tag

    Inserts a tag on the Permission

    :param permission_id: The permission unique identifier. E.g PERM001
    :type permission_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)
