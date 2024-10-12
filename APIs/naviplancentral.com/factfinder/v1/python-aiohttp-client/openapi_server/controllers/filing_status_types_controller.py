from typing import List, Dict
from aiohttp import web

from openapi_server.models.filing_status_type_model import FilingStatusTypeModel
from openapi_server.models.filing_status_types_model import FilingStatusTypesModel
from openapi_server import util


async def filing_status_types_get_by_country(request: web.Request, country) -> web.Response:
    """filing_status_types_get_by_country

    Description: This operation retrieves all Filing Status Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Filing Status Types including id and type description.

    :param country: The country used to filter Filing Status Types
    :type country: str

    """
    return web.Response(status=200)


async def filing_status_types_get_by_id(request: web.Request, id) -> web.Response:
    """filing_status_types_get_by_id

    Description: This operation retrieves all Filing Status Type for the specified id.&lt;br /&gt;                Purpose: Provides access to the Filing Status Types including id and type description.

    :param id: The ID of Filing Status Type used to retreive the Filing Status Type information
    :type id: int

    """
    return web.Response(status=200)
