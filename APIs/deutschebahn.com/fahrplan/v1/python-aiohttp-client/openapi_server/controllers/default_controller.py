from typing import List, Dict
from aiohttp import web

from openapi_server.models.board_response import BoardResponse
from openapi_server.models.error_model import ErrorModel
from openapi_server.models.journey_response import JourneyResponse
from openapi_server.models.location_response import LocationResponse
from openapi_server import util


async def arrival_board_id_get(request: web.Request, id, _date) -> web.Response:
    """Get arrival board of a location

    Get arrival board at a given location at a given daten and time.

    :param id: Id of location. Use attribute &#39;id&#39; from the result of &#39;location&#39;
    :type id: str
    :param _date: Date and time in ISO-8601 format, yyyy-mm-ddThh:mm:ss, example: 2017-04-01 or 2017-04-01T10:30
    :type _date: str

    """
    return web.Response(status=200)


async def departure_board_id_get(request: web.Request, id, _date) -> web.Response:
    """Get departure board of a location

    Get departure board at a given location at a given daten and time.

    :param id: Id of a location. Use attribute &#39;id&#39; from the result of &#39;location&#39;
    :type id: str
    :param _date: Date and time in ISO-8601 format, yyyy-mm-ddThh:mm:ss, example: 2017-04-01 or 2017-04-01T10:30
    :type _date: str

    """
    return web.Response(status=200)


async def journey_details_id_get(request: web.Request, id) -> web.Response:
    """Get details about a single journey

    Retrieve details of a journey. The id of journey should come from an arrival board or a departure board.

    :param id: Id of a journey. Use attribute &#39;detailsId&#39; from the result of  &#39;arrivalBoard&#39; or &#39;departureBoard&#39;
    :type id: str

    """
    return web.Response(status=200)


async def location_name_get(request: web.Request, name) -> web.Response:
    """Get location information

    Get information about locations matching the given name or name fragment

    :param name: Name or name fragment of a location
    :type name: str

    """
    return web.Response(status=200)
