from typing import List, Dict
from aiohttp import web

from openapi_server.models.graph_error import GraphError
from openapi_server.models.key_credential_list_result import KeyCredentialListResult
from openapi_server.models.key_credentials_update_parameters import KeyCredentialsUpdateParameters
from openapi_server import util


async def service_principals_list_key_credentials(request: web.Request, object_id, api_version, tenant_id) -> web.Response:
    """service_principals_list_key_credentials

    Get the keyCredentials associated with the specified service principal.

    :param object_id: The object ID of the service principal for which to get keyCredentials.
    :type object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str

    """
    return web.Response(status=200)


async def service_principals_update_key_credentials(request: web.Request, object_id, api_version, tenant_id, body) -> web.Response:
    """service_principals_update_key_credentials

    Update the keyCredentials associated with a service principal.

    :param object_id: The object ID for which to get service principal information.
    :type object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str
    :param body: Parameters to update the keyCredentials of an existing service principal.
    :type body: dict | bytes

    """
    body = KeyCredentialsUpdateParameters.from_dict(body)
    return web.Response(status=200)
