from typing import List, Dict
from aiohttp import web

from openapi_server.models.apii_paged_response_authorization_codes_shared_models_category import APIIPagedResponseAuthorizationCodesSharedModelsCategory
from openapi_server.models.apii_paged_response_authorization_codes_shared_models_category_user_report import APIIPagedResponseAuthorizationCodesSharedModelsCategoryUserReport
from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.authorization_codes_shared_models_category import AuthorizationCodesSharedModelsCategory
from openapi_server import util


async def authorization_categories_add_user(request: web.Request, id, user_id) -> web.Response:
    """Add a category that a user can see.

    No Documentation Found.

    :param id: 
    :type id: str
    :param user_id: 
    :type user_id: int

    """
    return web.Response(status=200)


async def authorization_categories_delete(request: web.Request, id) -> web.Response:
    """Remove an authorization category.

    No Documentation Found.

    :param id: The ID of the authorization category.
    :type id: str

    """
    return web.Response(status=200)


async def authorization_categories_get(request: web.Request, limit=None, offset=None, user_id=None, definition_id=None) -> web.Response:
    """Get authorization categories.

    No Documentation Found.

    :param limit: Optional. The page limit.  If not specified, the default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset.  If not specified, the default page offset is 0.
    :type offset: int
    :param user_id: Optional. Filter by categories visible to the provided user with the provided userID.
    :type user_id: int
    :param definition_id: Optional. Filter by categories containing a definition with the provided ID.
    :type definition_id: str

    """
    return web.Response(status=200)


async def authorization_categories_get_users(request: web.Request, limit=None, offset=None, user_ids=None, category_ids=None, include_categories=None, include_users=None, user_search=None) -> web.Response:
    """Returns a report of access that users have to Authorization Categories.

    No Documentation Found.

    :param limit: Optional. Defaults to 10.
    :type limit: int
    :param offset: Optional. Defaults to 0.
    :type offset: int
    :param user_ids: Optional. Includes only users with IDs on the provided comma-separated list.
    :type user_ids: str
    :param category_ids: Optional. Includes only users with categories with IDs on the provided comma-separated list.
    :type category_ids: str
    :param include_categories: If true, include full Authorization Category detail. Defaults to false.
    :type include_categories: bool
    :param include_users: If true, include full User detail. Defaults to false.
    :type include_users: bool
    :param user_search: Optional. Includes only users with a Name, Username, or Email containing the provided value.
    :type user_search: str

    """
    return web.Response(status=200)


async def authorization_categories_post(request: web.Request, body) -> web.Response:
    """Add an authorization category.

    No Documentation Found.

    :param body: An authorization category.
    :type body: dict | bytes

    """
    body = AuthorizationCodesSharedModelsCategory.from_dict(body)
    return web.Response(status=200)


async def authorization_categories_put(request: web.Request, id, body) -> web.Response:
    """Update an authorization category.

    No Documentation Found.

    :param id: 
    :type id: str
    :param body: An authorization category.
    :type body: dict | bytes

    """
    body = AuthorizationCodesSharedModelsCategory.from_dict(body)
    return web.Response(status=200)


async def authorization_categories_remove_user(request: web.Request, id, user_id) -> web.Response:
    """Deletes a category a user could see.

    No Documentation Found.

    :param id: 
    :type id: str
    :param user_id: 
    :type user_id: int

    """
    return web.Response(status=200)
