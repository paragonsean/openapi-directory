from typing import List, Dict
from aiohttp import web

from openapi_server.models.patch_organization_request import PatchOrganizationRequest
from openapi_server import util


async def get_organization(request: web.Request, id, include_locations=None) -> web.Response:
    """get_organization

    Get one organization&#39;s data by id

    :param id: ID of organization that needs to be fetched
    :type id: str
    :param include_locations: Populate locations
    :type include_locations: bool

    """
    return web.Response(status=200)


async def get_organizations(request: web.Request, paginate_limit=None, paginate_page=None, paginate_enabled=None, sort_by=None, sort_order=None, created_at_gte=None, created_at_lte=None, updated_at_gte=None, updated_at_lte=None, include_locations=None) -> web.Response:
    """get_organizations

    Get an array of all Organizations

    :param paginate_limit: Number of results per page
    :type paginate_limit: int
    :param paginate_page: The queried page index
    :type paginate_page: str
    :param paginate_enabled: Enable pagination
    :type paginate_enabled: bool
    :param sort_by: Sort data by this key
    :type sort_by: str
    :param sort_order: asc to sort ascending (default is desc - descending)
    :type sort_order: str
    :param created_at_gte: Date as ISO String
    :type created_at_gte: str
    :param created_at_lte: Date as ISO String
    :type created_at_lte: str
    :param updated_at_gte: Date as ISO String
    :type updated_at_gte: str
    :param updated_at_lte: Date as ISO String
    :type updated_at_lte: str
    :param include_locations: Populate locations
    :type include_locations: bool

    """
    created_at_gte = util.deserialize_datetime(created_at_gte)
    created_at_lte = util.deserialize_datetime(created_at_lte)
    updated_at_gte = util.deserialize_datetime(updated_at_gte)
    updated_at_lte = util.deserialize_datetime(updated_at_lte)
    return web.Response(status=200)


async def patch_organization(request: web.Request, id, body) -> web.Response:
    """patch_organization

    Update an organization&#39;s data

    :param id: ID of organization that needs to be updated
    :type id: str
    :param body: Include organization properties to create here
    :type body: dict | bytes

    """
    body = PatchOrganizationRequest.from_dict(body)
    return web.Response(status=200)
