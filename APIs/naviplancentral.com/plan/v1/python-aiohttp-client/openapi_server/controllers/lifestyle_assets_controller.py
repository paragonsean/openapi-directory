from typing import List, Dict
from aiohttp import web

from openapi_server.models.lifestyle_asset_model import LifestyleAssetModel
from openapi_server.models.lifestyle_assets_model import LifestyleAssetsModel
from openapi_server import util


async def lifestyle_assets_get_by_id_planid(request: web.Request, id, plan_id) -> web.Response:
    """Retrieve lifestyle assets

    This operation retrieves a lifestyle asset from the plan.

    :param id: ID of lifestyle asset to retrieve
    :type id: int
    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)


async def lifestyle_assets_get_by_planid(request: web.Request, plan_id) -> web.Response:
    """Retrieve lifestyle assets

    This operation retrieves a list of all of the lifestyle assets in the plan.

    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)
