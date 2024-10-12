from typing import List, Dict
from aiohttp import web

from openapi_server.models.tenant import Tenant
from openapi_server import util


async def configuration_add(request: web.Request, api_version) -> web.Response:
    """configuration_add

    Onboards a tenant in Azure Active Directory Connect Health.

    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def configuration_get(request: web.Request, api_version) -> web.Response:
    """configuration_get

    Gets the details of a tenant onboarded to Azure Active Directory Connect Health.

    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def configuration_update(request: web.Request, api_version, tenant) -> web.Response:
    """configuration_update

    Updates tenant properties for tenants onboarded to Azure Active Directory Connect Health.

    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param tenant: The tenant object with the properties set to the updated value.
    :type tenant: dict | bytes

    """
    tenant = Tenant.from_dict(tenant)
    return web.Response(status=200)
