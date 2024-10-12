from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_asset(request: web.Request, asset_id, aliases=None) -> web.Response:
    """Asset Detail

    Return the content of the selected asset.

    :param asset_id: A asset ID filter for the schedule collection. This can be a reference to any type of asset i.e. movie, season, series or episode.
    :type asset_id: str
    :param aliases: Flag to display Legacy and Provider Ids.
    :type aliases: bool

    """
    return web.Response(status=200)


async def get_asset_contributors(request: web.Request, asset_id, aliases=None) -> web.Response:
    """Asset Contributors

    Return the contributors of the selected asset.

    :param asset_id: A asset ID filter for the schedule collection. This can be a reference to any type of asset i.e. movie, season, series or episode.
    :type asset_id: str
    :param aliases: Flag to display Legacy and Provider Ids.
    :type aliases: bool

    """
    return web.Response(status=200)


async def list_assets(request: web.Request, updated_after=None, limit=None, aliases=None) -> web.Response:
    """Asset Collection

    Return a collection of Assets.

    :param updated_after: Updated After
    :type updated_after: str
    :param limit: Limit the the number of items to be returned per page. For example: 5.
    :type limit: int
    :param aliases: Flag to display Legacy and Provider Ids.
    :type aliases: bool

    """
    return web.Response(status=200)
