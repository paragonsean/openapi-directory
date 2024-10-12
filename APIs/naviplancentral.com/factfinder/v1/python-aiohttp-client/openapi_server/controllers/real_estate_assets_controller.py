from typing import List, Dict
from aiohttp import web

from openapi_server.models.real_estate_asset_model import RealEstateAssetModel
from openapi_server.models.real_estate_asset_with_id_model import RealEstateAssetWithIdModel
from openapi_server.models.real_estate_assets_model import RealEstateAssetsModel
from openapi_server import util


async def real_estate_assets_delete_by_id(request: web.Request, id) -> web.Response:
    """real_estate_assets_delete_by_id

    Description: The operation removes a Real Estate Asset tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Real Estate Asset from a Fact Finder.

    :param id: The Real Estate Asset ID used to identify which Real Estate Asset to remove
    :type id: int

    """
    return web.Response(status=200)


async def real_estate_assets_get_by_id(request: web.Request, id) -> web.Response:
    """real_estate_assets_get_by_id

    Description: This operation retrieves a single Real Estate Asset for the specified Real Estate Asset ID.&lt;br /&gt;                Purpose: Provides access to the Real Estate Asset including description and market value.

    :param id: The ID of the Real Estate Asset used to retreive the Real Estate Asset
    :type id: int

    """
    return web.Response(status=200)


async def real_estate_assets_get_real_estate_assets_by_fact_finder_id_by_factfinderid(request: web.Request, fact_finder_id) -> web.Response:
    """real_estate_assets_get_real_estate_assets_by_fact_finder_id_by_factfinderid

    Description: This operation retrieves all Real Estate Assets for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Real Estate Assets including description and market value.

    :param fact_finder_id: The ID of the Fact Finder used to retrieve Real Estate Assets
    :type fact_finder_id: int

    """
    return web.Response(status=200)


async def real_estate_assets_post_by_model(request: web.Request, model) -> web.Response:
    """real_estate_assets_post_by_model

    Description: The operation creates a Real Estate Asset.&lt;br /&gt;                Purpose: Allows for creation of Real Estate Assets on a Fact Finder.

    :param model: The Real Estate Asset to be added to the Fact Finder
    :type model: dict | bytes

    """
    model = RealEstateAssetModel.from_dict(model)
    return web.Response(status=200)


async def real_estate_assets_put_by_id_model(request: web.Request, id, model) -> web.Response:
    """real_estate_assets_put_by_id_model

    Description: The operation updates a Real Estate Asset.&lt;br /&gt;                Purpose: Allows for complete replacement of a Real Estate Asset on a Fact Finder.

    :param id: The existing Real Estate Asset ID used to identify which Real Estate Asset to update
    :type id: int
    :param model: The Real Estate Asset to be updated on a Fact Finder
    :type model: dict | bytes

    """
    model = RealEstateAssetModel.from_dict(model)
    return web.Response(status=200)
