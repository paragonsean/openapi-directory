from typing import List, Dict
from aiohttp import web

from openapi_server.models.graph_error import GraphError
from openapi_server.models.key_credential_list_result import KeyCredentialListResult
from openapi_server.models.key_credentials_update_parameters import KeyCredentialsUpdateParameters
from openapi_server import util


async def applications_list_key_credentials(request: web.Request, application_object_id, api_version, tenant_id) -> web.Response:
    """applications_list_key_credentials

    Get the keyCredentials associated with an application.

    :param application_object_id: Application object ID.
    :type application_object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str

    """
    return web.Response(status=200)


async def applications_update_key_credentials(request: web.Request, application_object_id, api_version, tenant_id, body) -> web.Response:
    """applications_update_key_credentials

    Update the keyCredentials associated with an application.

    :param application_object_id: Application object ID.
    :type application_object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str
    :param body: Parameters to update the keyCredentials of an existing application.
    :type body: dict | bytes

    """
    body = KeyCredentialsUpdateParameters.from_dict(body)
    return web.Response(status=200)
