from typing import List, Dict
from aiohttp import web

from openapi_server.models.state_province_model import StateProvinceModel
from openapi_server.models.states_provinces_model import StatesProvincesModel
from openapi_server import util


async def states_provinces_get_by_country(request: web.Request, country) -> web.Response:
    """states_provinces_get_by_country

    Description: This operation retrieves all States and Provinces for the specified country.&lt;br /&gt;                Purpose: Provides access to the States and Provinces.

    :param country: The country used to filter States and Provinces
    :type country: str

    """
    return web.Response(status=200)


async def states_provinces_get_by_id(request: web.Request, id) -> web.Response:
    """states_provinces_get_by_id

    Description: This operation retrieves the States and Provinces for the specified id.&lt;br /&gt;                Purpose: Provides access to the States and Provinces.

    :param id: The ID of the State or Province used to retreive the State or Province information
    :type id: int

    """
    return web.Response(status=200)
