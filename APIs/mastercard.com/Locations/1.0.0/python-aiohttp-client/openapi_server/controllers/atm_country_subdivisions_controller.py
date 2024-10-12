from typing import List, Dict
from aiohttp import web

from openapi_server.models.country_subdivision_response import CountrySubdivisionResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def atms_v1_countrysubdivision_get(request: web.Request, country) -> web.Response:
    """Returns country subdivisions that have ATM locations.  A country subdivision is a segment within a country (ex  state or province). Country subdivisions are only available for the US and Canada.

    Returns country subdivisions that have ATM locations.  A country subdivision is a segment within a country (ex  state or province). Country subdivisions are only available for the US and Canada. 

    :param country: Any three digit country code as defined in ISO 3166-1.  \&quot;USA\&quot; or \&quot;CAN\&quot;
    :type country: str

    """
    return web.Response(status=200)
