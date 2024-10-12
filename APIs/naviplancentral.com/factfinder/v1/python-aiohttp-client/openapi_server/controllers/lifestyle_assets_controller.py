from typing import List, Dict
from aiohttp import web

from openapi_server.models.lifestyle_asset_model import LifestyleAssetModel
from openapi_server.models.lifestyle_asset_with_id_model import LifestyleAssetWithIdModel
from openapi_server.models.lifestyle_assets_model import LifestyleAssetsModel
from openapi_server import util


async def lifestyle_assets_delete_by_id(request: web.Request, id) -> web.Response:
    """lifestyle_assets_delete_by_id

    Description: The operation removes a Lifestyle Asset tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Lifestyle Asset from a Fact Finder.

    :param id: The Lifestyle Asset ID used to identify which Lifestyle Asset to remove
    :type id: int

    """
    return web.Response(status=200)


async def lifestyle_assets_get_by_id(request: web.Request, id) -> web.Response:
    """lifestyle_assets_get_by_id

    Description: This operation retrieves a single Lifestyle Asset for the specified Lifestyle Asset ID.&lt;br /&gt;                Purpose: Provides access to the Lifestyle Asset including description and market value.

    :param id: The ID of the Lifestyle Asset used to retreive the Lifestyle Asset
    :type id: int

    """
    return web.Response(status=200)


async def lifestyle_assets_get_lifestyle_assets_by_fact_finder_id_by_factfinderid(request: web.Request, fact_finder_id) -> web.Response:
    """lifestyle_assets_get_lifestyle_assets_by_fact_finder_id_by_factfinderid

    Description: This operation retrieves all Lifestyle Assets for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Lifestyle Assets including description and market value.

    :param fact_finder_id: The ID of the Fact Finder used to retrieve Lifestyle Assets
    :type fact_finder_id: int

    """
    return web.Response(status=200)


async def lifestyle_assets_post_by_model(request: web.Request, model) -> web.Response:
    """lifestyle_assets_post_by_model

    Description: The operation creates a Lifestyle Asset.&lt;br /&gt;                Purpose: Allows for creation of Lifestyle Assets on a Fact Finder.

    :param model: The Lifestyle Asset to be added to the Fact Finder
    :type model: dict | bytes

    """
    model = LifestyleAssetModel.from_dict(model)
    return web.Response(status=200)


async def lifestyle_assets_put_by_id_model(request: web.Request, id, model) -> web.Response:
    """lifestyle_assets_put_by_id_model

    Description: The operation updates a Lifestyle Asset.&lt;br /&gt;                Purpose: Allows for complete replacement of a Lifestyle Asset on a Fact Finder.

    :param id: The existing Lifestyle Asset ID used to identify which Lifestyle Asset to update
    :type id: int
    :param model: The Lifestyle Asset to be updated on a Fact Finder
    :type model: dict | bytes

    """
    model = LifestyleAssetModel.from_dict(model)
    return web.Response(status=200)
