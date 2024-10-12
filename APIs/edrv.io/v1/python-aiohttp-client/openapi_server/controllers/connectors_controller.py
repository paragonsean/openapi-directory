from typing import List, Dict
from aiohttp import web

from openapi_server.models.patch_charge_station200_response import PatchChargeStation200Response
from openapi_server.models.post_connectors_request import PostConnectorsRequest
from openapi_server import util


async def delete_connector(request: web.Request, id) -> web.Response:
    """delete_connector

    Delete a connector

    :param id: The connector id that needs to be deleted
    :type id: str

    """
    return web.Response(status=200)


async def get_connector(request: web.Request, id, include_evse=None, include_organization=None, include_rate=None) -> web.Response:
    """get_connector

    Get a connector

    :param id: ID of connector that needs to be fetched
    :type id: str
    :param include_evse: Populate evse
    :type include_evse: bool
    :param include_organization: Populate organization
    :type include_organization: bool
    :param include_rate: Populate rate
    :type include_rate: bool

    """
    return web.Response(status=200)


async def get_connectors(request: web.Request, paginate_limit=None, paginate_page=None, paginate_enabled=None, sort_by=None, sort_order=None, created_at_gte=None, created_at_lte=None, updated_at_gte=None, updated_at_lte=None, include_evse=None, include_organization=None, include_rate=None) -> web.Response:
    """get_connectors

    List connectors

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
    :param include_evse: Populate evse
    :type include_evse: bool
    :param include_organization: Populate organization
    :type include_organization: bool
    :param include_rate: Populate rate
    :type include_rate: bool

    """
    created_at_gte = util.deserialize_datetime(created_at_gte)
    created_at_lte = util.deserialize_datetime(created_at_lte)
    updated_at_gte = util.deserialize_datetime(updated_at_gte)
    updated_at_lte = util.deserialize_datetime(updated_at_lte)
    return web.Response(status=200)


async def patch_connector(request: web.Request, id, body) -> web.Response:
    """patch_connector

    Update a connector&#39;s data

    :param id: ID of connector that needs to be updated
    :type id: str
    :param body: Include connector properties to update here
    :type body: dict | bytes

    """
    body = PostConnectorsRequest.from_dict(body)
    return web.Response(status=200)


async def post_connectors(request: web.Request, body) -> web.Response:
    """post_connectors

    Create a new connector

    :param body: Include Connector properties to create here
    :type body: dict | bytes

    """
    body = PostConnectorsRequest.from_dict(body)
    return web.Response(status=200)
