from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_information_contract import AccessInformationContract
from openapi_server.models.tenant_access_update_default_response import TenantAccessUpdateDefaultResponse
from openapi_server import util


async def tenant_access_git_get(request: web.Request, api_version, access_name) -> web.Response:
    """tenant_access_git_get

    Gets the Git access configuration for the tenant.

    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param access_name: The identifier of the Access configuration.
    :type access_name: str

    """
    return web.Response(status=200)


async def tenant_access_git_regenerate_primary_key(request: web.Request, api_version, access_name) -> web.Response:
    """tenant_access_git_regenerate_primary_key

    Regenerate primary access key for GIT.

    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param access_name: The identifier of the Access configuration.
    :type access_name: str

    """
    return web.Response(status=200)


async def tenant_access_git_regenerate_secondary_key(request: web.Request, api_version, access_name) -> web.Response:
    """tenant_access_git_regenerate_secondary_key

    Regenerate secondary access key for GIT.

    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param access_name: The identifier of the Access configuration.
    :type access_name: str

    """
    return web.Response(status=200)
