from typing import List, Dict
from aiohttp import web

from openapi_server.models.id_provider_auth_domain_info import IdProviderAuthDomainInfo
from openapi_server.models.id_provider_auth_domain_info_update import IdProviderAuthDomainInfoUpdate
from openapi_server.models.id_provider_auth_domain_summary import IdProviderAuthDomainSummary
from openapi_server.models.id_provider_auth_domain_summary_list_response import IdProviderAuthDomainSummaryListResponse
from openapi_server import util


async def create_id_provider_auth_domain(request: web.Request, body) -> web.Response:
    """Add a new IdP authentication domain

    Add a new IdP authentication domain.

    :param body: Information for joining an IdP authentication domain.
    :type body: dict | bytes

    """
    body = IdProviderAuthDomainInfo.from_dict(body)
    return web.Response(status=200)


async def delete_id_provider_auth_domain(request: web.Request, id) -> web.Response:
    """Delete an IdP authentication domain for the given ID

    Delete an IdP authentication domain for the given ID.

    :param id: ID of the IdP authentication domain to be deleted.
    :type id: str

    """
    return web.Response(status=200)


async def get_id_provider_auth_domain(request: web.Request, id) -> web.Response:
    """Get an IdP authentication domain for the given id

    Get an IdP authentication domain for the given id.

    :param id: ID of the IdP Authentication Domain to be retrieved.
    :type id: str

    """
    return web.Response(status=200)


async def query_id_provider_auth_domain(request: web.Request, ) -> web.Response:
    """Get a list of IdP authentication domains

    Get a list of IdP authentication domains.


    """
    return web.Response(status=200)


async def update_id_provider_auth_domain(request: web.Request, id, body) -> web.Response:
    """Update an existing IdP authentication domain

    Update an existing IdP authentication domain.

    :param id: ID of the IdP authentication domain to be updated.
    :type id: str
    :param body: Information for updating an IdP authentication domain.
    :type body: dict | bytes

    """
    body = IdProviderAuthDomainInfoUpdate.from_dict(body)
    return web.Response(status=200)
