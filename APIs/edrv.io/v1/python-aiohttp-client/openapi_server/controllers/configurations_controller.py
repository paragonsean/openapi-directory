from typing import List, Dict
from aiohttp import web

from openapi_server.models.patch_charge_station200_response import PatchChargeStation200Response
from openapi_server.models.post_configurations_request import PostConfigurationsRequest
from openapi_server import util


async def get_configuration(request: web.Request, id) -> web.Response:
    """get_configuration

    Get one Configuration data

    :param id: ID of Configuration that needs to be fetched
    :type id: str

    """
    return web.Response(status=200)


async def get_configurations(request: web.Request, paginate_limit=None, paginate_page=None, paginate_enabled=None, sort_by=None, sort_order=None, created_at_gte=None, created_at_lte=None, updated_at_gte=None, updated_at_lte=None) -> web.Response:
    """get_configurations

    Get Configurations data

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

    """
    created_at_gte = util.deserialize_datetime(created_at_gte)
    created_at_lte = util.deserialize_datetime(created_at_lte)
    updated_at_gte = util.deserialize_datetime(updated_at_gte)
    updated_at_lte = util.deserialize_datetime(updated_at_lte)
    return web.Response(status=200)


async def post_configurations(request: web.Request, body) -> web.Response:
    """post_configurations

    Create connector with parameters

    :param body: Include Configuration properties to create here
    :type body: dict | bytes

    """
    body = PostConfigurationsRequest.from_dict(body)
    return web.Response(status=200)
