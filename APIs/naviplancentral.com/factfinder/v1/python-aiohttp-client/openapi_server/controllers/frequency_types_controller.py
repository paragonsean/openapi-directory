from typing import List, Dict
from aiohttp import web

from openapi_server.models.frequency_type_model import FrequencyTypeModel
from openapi_server.models.frequency_types_model import FrequencyTypesModel
from openapi_server import util


async def frequency_types_get_by_entity_country(request: web.Request, entity, country) -> web.Response:
    """frequency_types_get_by_entity_country

    Description: This operation retrieves all Frequency Types for the specified country and entity.&lt;br /&gt;                Purpose: Provides access to the Frequency Types including id and type description.

    :param entity: The entity used to filter Frequency Types
    :type entity: str
    :param country: The country used to filter Frequency Types
    :type country: str

    """
    return web.Response(status=200)


async def frequency_types_get_by_id(request: web.Request, id) -> web.Response:
    """frequency_types_get_by_id

    Description: This operation retrieves the Frequency Type for the specified id.&lt;br /&gt;                Purpose: Provides access to the Frequency Types including id and type description.

    :param id: The ID of Frequency Type used to retreive the Frequency Type information
    :type id: int

    """
    return web.Response(status=200)
