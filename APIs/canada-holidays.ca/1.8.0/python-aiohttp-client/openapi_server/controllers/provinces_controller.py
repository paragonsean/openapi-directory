from typing import List, Dict
from aiohttp import web

from openapi_server.models.holiday400_response import Holiday400Response
from openapi_server.models.province200_response import Province200Response
from openapi_server.models.provinces200_response import Provinces200Response
from openapi_server import util


async def province(request: web.Request, province_id, year=None, optional=None) -> web.Response:
    """Get a province or territory by abbreviation

    Returns a Canadian province or territory with its associated holidays. Returns a 404 response for invalid abbreviations.

    :param province_id: A Canadian province abbreviation
    :type province_id: str
    :param year: A calendar year
    :type year: int
    :param optional: A boolean parameter (AB and BC only). If false or 0 (default), will return only legislated holidays. If true or 1, will return optional holidays from Alberta and BC.
    :type optional: str

    """
    return web.Response(status=200)


async def provinces(request: web.Request, year=None, optional=None) -> web.Response:
    """Get all provinces

    Returns provinces and territories in Canada. Each province or territory lists its associated holidays.

    :param year: A calendar year
    :type year: int
    :param optional: A boolean parameter. If false or 0 (default), will return only legislated holidays. If true or 1, will return optional holidays from Alberta and BC.
    :type optional: str

    """
    return web.Response(status=200)
