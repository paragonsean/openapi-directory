from typing import List, Dict
from aiohttp import web

from openapi_server.models.graph_error import GraphError
from openapi_server.models.password_credential_list_result import PasswordCredentialListResult
from openapi_server.models.password_credentials_update_parameters import PasswordCredentialsUpdateParameters
from openapi_server import util


async def service_principals_list_password_credentials(request: web.Request, object_id, api_version, tenant_id) -> web.Response:
    """service_principals_list_password_credentials

    Gets the passwordCredentials associated with a service principal.

    :param object_id: The object ID of the service principal.
    :type object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str

    """
    return web.Response(status=200)


async def service_principals_update_password_credentials(request: web.Request, object_id, api_version, tenant_id, body) -> web.Response:
    """service_principals_update_password_credentials

    Updates the passwordCredentials associated with a service principal.

    :param object_id: The object ID of the service principal.
    :type object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str
    :param body: Parameters to update the passwordCredentials of an existing service principal.
    :type body: dict | bytes

    """
    body = PasswordCredentialsUpdateParameters.from_dict(body)
    return web.Response(status=200)
