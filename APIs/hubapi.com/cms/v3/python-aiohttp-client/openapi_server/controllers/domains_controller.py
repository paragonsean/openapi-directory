from typing import List, Dict
from aiohttp import web

from openapi_server.models.collection_response_with_total_domain_forward_paging import CollectionResponseWithTotalDomainForwardPaging
from openapi_server.models.domain import Domain
from openapi_server.models.error import Error
from openapi_server import util


async def get_cms_v3_domains_domain_id_get_by_id(request: web.Request, domain_id) -> web.Response:
    """Get a single domain

    Returns a single domains with the id specified.

    :param domain_id: The unique ID of the domain.
    :type domain_id: str

    """
    return web.Response(status=200)


async def get_cms_v3_domains_get_page(request: web.Request, created_at=None, created_after=None, created_before=None, updated_at=None, updated_after=None, updated_before=None, sort=None, after=None, limit=None, archived=None) -> web.Response:
    """Get current domains

    Returns all existing domains that have been created. Results can be limited and filtered by creation or updated date.

    :param created_at: Only return domains created at this date.
    :type created_at: str
    :param created_after: Only return domains created after this date.
    :type created_after: str
    :param created_before: Only return domains created before this date.
    :type created_before: str
    :param updated_at: Only return domains updated at this date.
    :type updated_at: str
    :param updated_after: Only return domains updated after this date.
    :type updated_after: str
    :param updated_before: Only return domains updated before this date.
    :type updated_before: str
    :param sort: 
    :type sort: List[str]
    :param after: The paging cursor token of the last successfully read resource will be returned as the &#x60;paging.next.after&#x60; JSON property of a paged response containing more results.
    :type after: str
    :param limit: Maximum number of results per page.
    :type limit: int
    :param archived: Whether to return only results that have been archived.
    :type archived: bool

    """
    created_at = util.deserialize_datetime(created_at)
    created_after = util.deserialize_datetime(created_after)
    created_before = util.deserialize_datetime(created_before)
    updated_at = util.deserialize_datetime(updated_at)
    updated_after = util.deserialize_datetime(updated_after)
    updated_before = util.deserialize_datetime(updated_before)
    return web.Response(status=200)
