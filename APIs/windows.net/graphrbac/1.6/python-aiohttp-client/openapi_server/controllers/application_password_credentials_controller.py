from typing import List, Dict
from aiohttp import web

from openapi_server.models.graph_error import GraphError
from openapi_server.models.password_credential_list_result import PasswordCredentialListResult
from openapi_server.models.password_credentials_update_parameters import PasswordCredentialsUpdateParameters
from openapi_server import util


async def applications_list_password_credentials(request: web.Request, application_object_id, api_version, tenant_id) -> web.Response:
    """applications_list_password_credentials

    Get the passwordCredentials associated with an application.

    :param application_object_id: Application object ID.
    :type application_object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str

    """
    return web.Response(status=200)


async def applications_update_password_credentials(request: web.Request, application_object_id, api_version, tenant_id, body) -> web.Response:
    """applications_update_password_credentials

    Update passwordCredentials associated with an application.

    :param application_object_id: Application object ID.
    :type application_object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str
    :param body: Parameters to update passwordCredentials of an existing application.
    :type body: dict | bytes

    """
    body = PasswordCredentialsUpdateParameters.from_dict(body)
    return web.Response(status=200)
