from typing import List, Dict
from aiohttp import web

from openapi_server.models.apii_paged_response_authorization_codes_shared_models_authorization_code import APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationCode
from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.authorization_codes_shared_models_authorization_code import AuthorizationCodesSharedModelsAuthorizationCode
from openapi_server.models.authorization_codes_shared_models_authorization_contact_information import AuthorizationCodesSharedModelsAuthorizationContactInformation
from openapi_server.models.authorization_codes_shared_models_code_validation_model import AuthorizationCodesSharedModelsCodeValidationModel
from openapi_server import util


async def authorization_codes_delete_authorization_code(request: web.Request, id) -> web.Response:
    """Hide an authorization code.

    No Documentation Found.

    :param id: The id of the authorization code.
    :type id: int

    """
    return web.Response(status=200)


async def authorization_codes_get_authorization_code(request: web.Request, id) -> web.Response:
    """Get an authorization code by its ID.

    No Documentation Found.

    :param id: The id of the authorization code.
    :type id: int

    """
    return web.Response(status=200)


async def authorization_codes_get_authorization_codes(request: web.Request, code=None, limit=None, offset=None, definition_id=None, created_by_user_id=None, deleted_by_user_id=None, include_deleted=None) -> web.Response:
    """Get authorization codes.

    Additional searches: validationParameters[Name]&#x3D;Value and dataParameters[Name]&#x3D;Value. These can be used to search for authorization codes that have been generated using specified values for data or validation parameters.

    :param code: Optional. If provided, searches for entities with the provided authorization code.
    :type code: str
    :param limit: Optional. The page limit.  If not specified, the default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset.  If not specified, the default page offset is 0.
    :type offset: int
    :param definition_id: Optional. If specified, filters codes by definition id.
    :type definition_id: str
    :param created_by_user_id: Optional. If specified, filters codes to those created by the given User ID.
    :type created_by_user_id: int
    :param deleted_by_user_id: Optional. If specified, filters codes to those deleted by the given User ID.
    :type deleted_by_user_id: int
    :param include_deleted: Optional. Whether to include deleted codes. &#39;False&#39; by default.
    :type include_deleted: bool

    """
    return web.Response(status=200)


async def authorization_codes_get_contact_information(request: web.Request, id) -> web.Response:
    """Get contact information for an authorization code.

    No Documentation Found.

    :param id: The id of the authorization code.
    :type id: int

    """
    return web.Response(status=200)


async def authorization_codes_post_authorization_code(request: web.Request, body) -> web.Response:
    """Generates an authorization code using the provided definition and parameters.

    No Documentation Found.

    :param body: The model from which to generate an authorization code.
    :type body: dict | bytes

    """
    body = AuthorizationCodesSharedModelsAuthorizationCode.from_dict(body)
    return web.Response(status=200)


async def authorization_codes_put_authorization_code(request: web.Request, id, body) -> web.Response:
    """Update an authorization code.

    No Documentation Found.

    :param id: The id of the authorization code.
    :type id: int
    :param body: The model from which to update an authorization code.
    :type body: dict | bytes

    """
    body = AuthorizationCodesSharedModelsAuthorizationCode.from_dict(body)
    return web.Response(status=200)


async def authorization_codes_validate_authorization_code(request: web.Request, id) -> web.Response:
    """No Documentation Found.

    No Documentation Found.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)
