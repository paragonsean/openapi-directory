from typing import List, Dict
from aiohttp import web

from openapi_server.models.tenant_list_result import TenantListResult
from openapi_server import util


async def tenants_list(request: web.Request, api_version) -> web.Response:
    """tenants_list

    Gets the tenants for your account.

    :param api_version: The API version to use for the operation.
    :type api_version: str

    """
    return web.Response(status=200)
