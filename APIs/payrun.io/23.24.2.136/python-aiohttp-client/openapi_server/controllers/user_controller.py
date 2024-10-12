from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.tag import Tag
from openapi_server.models.user import User
from openapi_server import util


async def delete_user(request: web.Request, user_id, authorization, api_version) -> web.Response:
    """Deletes the user object

    Deletes the user object from the application

    :param user_id: The user unique identifier. E.g USER001
    :type user_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_user_tag_0(request: web.Request, user_id, tag_id, authorization, api_version) -> web.Response:
    """Delete user tag

    Deletes a tag from the user

    :param user_id: The user unique identifier. E.g USER001
    :type user_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_user_tags_0(request: web.Request, authorization, api_version) -> web.Response:
    """Get all user tags

    Get all tags from all users

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_users_with_tag_0(request: web.Request, tag_id, authorization, api_version) -> web.Response:
    """Get links to tagged users

    Gets the users with the specified tag

    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tag_from_user_0(request: web.Request, user_id, tag_id, authorization, api_version) -> web.Response:
    """Get user tag

    Gets a tag from the user

    :param user_id: The user unique identifier. E.g USER001
    :type user_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tags_from_user_0(request: web.Request, user_id, authorization, api_version) -> web.Response:
    """Get tags from user

    Gets all tags from the user

    :param user_id: The user unique identifier. E.g USER001
    :type user_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_user(request: web.Request, user_id, authorization, api_version) -> web.Response:
    """Gets the user object

    Gets the user object for application

    :param user_id: The user unique identifier. E.g USER001
    :type user_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_user_permissions_0(request: web.Request, user_id, authorization, api_version) -> web.Response:
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


async def get_users(request: web.Request, authorization, api_version) -> web.Response:
    """Gets all user objects

    Gets all user objects for application

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def patch_user(request: web.Request, user_id, authorization, api_version) -> web.Response:
    """Patch user object

    Patch the user object at the specified resource location

    :param user_id: The user unique identifier. E.g USER001
    :type user_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def post_user(request: web.Request, authorization, api_version) -> web.Response:
    """Post user object

    Post the new user object into the application

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_user(request: web.Request, user_id, authorization, api_version) -> web.Response:
    """Puts user object

    Puts the user object into the specified resource location

    :param user_id: The user unique identifier. E.g USER001
    :type user_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_user_tag_0(request: web.Request, user_id, tag_id, authorization, api_version) -> web.Response:
    """Insert user tag

    Inserts a tag on the user

    :param user_id: The user unique identifier. E.g USER001
    :type user_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)
