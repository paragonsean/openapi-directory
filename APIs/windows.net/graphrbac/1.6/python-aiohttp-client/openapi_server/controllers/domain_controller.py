from typing import List, Dict
from aiohttp import web

from openapi_server.models.domain import Domain
from openapi_server.models.domain_list_result import DomainListResult
from openapi_server import util


async def domains_get(request: web.Request, domain_name, api_version, tenant_id) -> web.Response:
    """domains_get

    Gets a specific domain in the current tenant.

    :param domain_name: name of the domain.
    :type domain_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str

    """
    return web.Response(status=200)


async def domains_list(request: web.Request, api_version, tenant_id, filter=None) -> web.Response:
    """domains_list

    Gets a list of domains for the current tenant.

    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str
    :param filter: The filter to apply to the operation.
    :type filter: str

    """
    return web.Response(status=200)
