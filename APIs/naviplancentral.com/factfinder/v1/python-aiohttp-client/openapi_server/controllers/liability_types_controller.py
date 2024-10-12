from typing import List, Dict
from aiohttp import web

from openapi_server.models.liability_type_model import LiabilityTypeModel
from openapi_server.models.liability_types_model import LiabilityTypesModel
from openapi_server import util


async def liability_types_get_by_country(request: web.Request, country) -> web.Response:
    """liability_types_get_by_country

    Description: This operation retrieves all Liability Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Liability Types including id and type description.

    :param country: The country used to filter Liability Types
    :type country: str

    """
    return web.Response(status=200)


async def liability_types_get_by_id(request: web.Request, id) -> web.Response:
    """liability_types_get_by_id

    Description: This operation retrieves the Liability Type for the specified id.&lt;br /&gt;                Purpose: Provides access to the Liability Types including id and type description.

    :param id: The ID of Liability Type used to retreive the Liability Type information
    :type id: int

    """
    return web.Response(status=200)
