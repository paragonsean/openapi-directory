from typing import List, Dict
from aiohttp import web

from openapi_server.models.code_full_entry import CodeFullEntry
from openapi_server.models.codes_list_response import CodesListResponse
from openapi_server import util


async def codes_get_code(request: web.Request, app_id, app_key, hotel_id, id) -> web.Response:
    """Get all the details for a specific code available for the hotel.

    Read the details about a specific code available for the defined hotel.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param hotel_id: The hotel id the code available for.
    :type hotel_id: int
    :param id: The code identifier you want to see details for.
    :type id: str

    """
    return web.Response(status=200)


async def codes_get_codes(request: web.Request, app_id, app_key, hotel_id, code=None, type=None) -> web.Response:
    """Get a list of codes for the specified hotel either filtered by type or code.

    With this call you can find codes for a hotel by type or code. By default and without any filter criteria              defined it will return you all available codes.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param hotel_id: The hotel id you are trying to find codes for.
    :type hotel_id: int
    :param code: Return all results matching the specified code. A code is unique in combination with the type              which means when you query for a code you could get multiple results each for a different type
    :type code: str
    :param type: Return all codes for the specified type
    :type type: str

    """
    return web.Response(status=200)
