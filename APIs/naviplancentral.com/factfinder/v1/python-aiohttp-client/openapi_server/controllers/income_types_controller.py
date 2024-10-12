from typing import List, Dict
from aiohttp import web

from openapi_server.models.income_type_model import IncomeTypeModel
from openapi_server.models.income_types_model import IncomeTypesModel
from openapi_server import util


async def income_types_get_by_country(request: web.Request, country) -> web.Response:
    """income_types_get_by_country

    Description: This operation retrieves all Income Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Income Types including id and type description.

    :param country: The country used to filter Income Types
    :type country: str

    """
    return web.Response(status=200)


async def income_types_get_by_id(request: web.Request, id) -> web.Response:
    """income_types_get_by_id

    Description: This operation retrieves the Income Type for the specified id.&lt;br /&gt;                Purpose: Provides access to the Income Types including id and type description.

    :param id: The ID of Income Type used to retreive the Income Type information
    :type id: int

    """
    return web.Response(status=200)
