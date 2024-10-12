from typing import List, Dict
from aiohttp import web

from openapi_server.models.info_public import InfoPublic
from openapi_server import util


async def get_database_info(request: web.Request, age_value=None, age_unit=None) -> web.Response:
    """Get database information

    Returns information about data used by diagnostic engine.

    :param age_value: age value
    :type age_value: int
    :param age_unit: unit in which age value was provided
    :type age_unit: str

    """
    return web.Response(status=200)
