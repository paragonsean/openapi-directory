from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_information_contract import AccessInformationContract
from openapi_server.models.access_information_update_parameters import AccessInformationUpdateParameters
from openapi_server.models.tenant_access_update_default_response import TenantAccessUpdateDefaultResponse
from openapi_server import util


async def tenant_access_get(request: web.Request, api_version, access_name) -> web.Response:
    """tenant_access_get

    Get tenant access information details.

    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param access_name: The identifier of the Access configuration.
    :type access_name: str

    """
    return web.Response(status=200)


async def tenant_access_regenerate_primary_key(request: web.Request, api_version, access_name) -> web.Response:
    """tenant_access_regenerate_primary_key

    Regenerate primary access key.

    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param access_name: The identifier of the Access configuration.
    :type access_name: str

    """
    return web.Response(status=200)


async def tenant_access_regenerate_secondary_key(request: web.Request, api_version, access_name) -> web.Response:
    """tenant_access_regenerate_secondary_key

    Regenerate secondary access key.

    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param access_name: The identifier of the Access configuration.
    :type access_name: str

    """
    return web.Response(status=200)


async def tenant_access_update(request: web.Request, access_name, if_match, api_version, parameters) -> web.Response:
    """tenant_access_update

    Update tenant access information details.

    :param access_name: The identifier of the Access configuration.
    :type access_name: str
    :param if_match: The entity state (Etag) version of the property to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: Parameters supplied to retrieve the Tenant Access Information.
    :type parameters: dict | bytes

    """
    parameters = AccessInformationUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
