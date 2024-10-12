from typing import List, Dict
from aiohttp import web

from openapi_server.models.identity_error_response import IdentityErrorResponse
from openapi_server.models.identity_token_response import IdentityTokenResponse
from openapi_server import util


async def identity_get_token(request: web.Request, metadata, resource, api_version, client_id=None, object_id=None, msi_res_id=None, authority=None, bypass_cache=None) -> web.Response:
    """identity_get_token

    Get a Token from Azure AD

    :param metadata: This must be set to &#39;true&#39;.
    :type metadata: str
    :param resource: This is the urlencoded identifier URI of the sink resource for the requested Azure AD token. The resulting token contains the corresponding aud for this resource.
    :type resource: str
    :param api_version: This is the API version to use.
    :type api_version: str
    :param client_id: This identifies, by Azure AD client id, a specific explicit identity to use when authenticating to Azure AD. Mutually exclusive with object_id and msi_res_id.
    :type client_id: str
    :param object_id: This identifies, by Azure AD object id, a specific explicit identity to use when authenticating to Azure AD. Mutually exclusive with client_id and msi_res_id.
    :type object_id: str
    :param msi_res_id: This identifies, by urlencoded ARM resource id, a specific explicit identity to use when authenticating to Azure AD. Mutually exclusive with client_id and object_id.
    :type msi_res_id: str
    :param authority: This indicates the authority to request AAD tokens from. Defaults to the known authority of the identity to be used.
    :type authority: str
    :param bypass_cache: If provided, the value must be &#39;true&#39;. This indicates to the server that the token must be retrieved from Azure AD and cannot be retrieved from an internal cache.
    :type bypass_cache: str

    """
    return web.Response(status=200)
