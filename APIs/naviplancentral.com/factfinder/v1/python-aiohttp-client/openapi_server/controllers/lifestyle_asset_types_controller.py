from typing import List, Dict
from aiohttp import web

from openapi_server.models.lifestyle_asset_type_model import LifestyleAssetTypeModel
from openapi_server.models.lifestyle_asset_types_model import LifestyleAssetTypesModel
from openapi_server import util


async def lifestyle_asset_types_get_by_country(request: web.Request, country) -> web.Response:
    """lifestyle_asset_types_get_by_country

    Description: This operation retrieves all Lifestyle Asset Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Lifestyle Asset Types including id and type description.

    :param country: The country used to filter Lifestyle Asset Types
    :type country: str

    """
    return web.Response(status=200)


async def lifestyle_asset_types_get_by_id(request: web.Request, id) -> web.Response:
    """lifestyle_asset_types_get_by_id

    Description: This operation retrieves the Lifestyle Asset Type for the specified id.&lt;br /&gt;                Purpose: Provides access to the Lifestyle Asset Types including id and type description.

    :param id: The ID of Lifestyle Asset Type used to retreive the Lifestyle Asset Type information
    :type id: int

    """
    return web.Response(status=200)
