from typing import List, Dict
from aiohttp import web

from openapi_server.models.apii_paged_response_authorization_codes_shared_models_authorization_code_definition import APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationCodeDefinition
from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.authorization_codes_shared_models_authorization_code_definition import AuthorizationCodesSharedModelsAuthorizationCodeDefinition
from openapi_server import util


async def api_v2_authorization_code_definitions_id_get(request: web.Request, id) -> web.Response:
    """Get an authorization code definition by its ID

    No Documentation Found.

    :param id: The ID of the authorization code definition.
    :type id: str

    """
    return web.Response(status=200)


async def authorization_code_definitions_add_category_to_definition(request: web.Request, id, category_id) -> web.Response:
    """Add a category to an authorizationCodeDefintion.

    No Documentation Found.

    :param id: 
    :type id: str
    :param category_id: A category ID, as a GUID.
    :type category_id: str

    """
    return web.Response(status=200)


async def authorization_code_definitions_delete_authorization_code_definition(request: web.Request, id) -> web.Response:
    """Disable an authorization code definition

    No Documentation Found.

    :param id: The ID of the authorization code definition.
    :type id: str

    """
    return web.Response(status=200)


async def authorization_code_definitions_get_authorization_code_definition(request: web.Request, limit=None, offset=None, name=None, created_by_user_id=None, deleted_by_user_id=None, include_deleted=None, category_id=None) -> web.Response:
    """Get authorization code definitions.

    Additional searches: validationFields[Name]&#x3D;true and dataFields[Name]&#x3D;true. These can be used to search for authorization code definitions that have the specified data or validation fields.

    :param limit: Optional. The page limit.  If not specified, the default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset.  If not specified, the default page offset is 0.
    :type offset: int
    :param name: Optional. If specified, filters definitions by name. Starting and ending wildcards (*) supported.
    :type name: str
    :param created_by_user_id: Optional. If specified, filters definitions to those created by the given User ID.
    :type created_by_user_id: int
    :param deleted_by_user_id: Optional. If specified, filters definitions to those deleted by the given User ID.
    :type deleted_by_user_id: int
    :param include_deleted: Optional. Whether to include deleted definitions. &#39;False&#39; by default.
    :type include_deleted: bool
    :param category_id: Optional. If specified, filters definitions with the designated categoryID.
    :type category_id: str

    """
    return web.Response(status=200)


async def authorization_code_definitions_post_authorization_code_definition(request: web.Request, body) -> web.Response:
    """Add an authorization code definition.

    No Documentation Found.

    :param body: An authorization code definition.
    :type body: dict | bytes

    """
    body = AuthorizationCodesSharedModelsAuthorizationCodeDefinition.from_dict(body)
    return web.Response(status=200)


async def authorization_code_definitions_put_authorization_code_definition(request: web.Request, id, body) -> web.Response:
    """Update an authorization code definition

    No Documentation Found.

    :param id: The ID of the authorization code definition.
    :type id: str
    :param body: An authorization code definition.
    :type body: dict | bytes

    """
    body = AuthorizationCodesSharedModelsAuthorizationCodeDefinition.from_dict(body)
    return web.Response(status=200)


async def authorization_code_definitions_remove_category_from_definition(request: web.Request, id, category_id) -> web.Response:
    """Deletes the category from the authorization code definition.

    No Documentation Found.

    :param id: 
    :type id: str
    :param category_id: A category ID, as a GUID.
    :type category_id: str

    """
    return web.Response(status=200)
