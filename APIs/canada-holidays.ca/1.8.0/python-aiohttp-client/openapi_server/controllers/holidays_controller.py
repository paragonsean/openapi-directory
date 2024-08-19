from typing import List, Dict
from aiohttp import web

from openapi_server.models.holiday200_response import Holiday200Response
from openapi_server.models.holiday400_response import Holiday400Response
from openapi_server.models.holidays200_response import Holidays200Response
from openapi_server import util


async def holiday(request: web.Request, holiday_id, year=None, optional=None) -> web.Response:
    """Get a holiday by id

    Returns one Canadian statutory holiday by integer id. Returns a 404 response for invalid ids.

    :param holiday_id: Primary key for a holiday
    :type holiday_id: int
    :param year: A calendar year
    :type year: int
    :param optional: A boolean parameter. If false or 0 (default), will return provinces for which this is a legislated holiday. If true or 1, will return provinces which optionally celebrate this holiday.
    :type optional: str

    """
    return web.Response(status=200)


async def holidays(request: web.Request, year=None, federal=None, optional=None) -> web.Response:
    """Get all holidays

    Returns Canadian public holidays. Each holiday lists the regions that observe it.

    :param year: A calendar year
    :type year: int
    :param federal: A boolean parameter. If true or 1, will return only federal holidays. If false or 0, will return no federal holidays.
    :type federal: str
    :param optional: A boolean parameter. If false or 0 (default), will return only legislated holidays. If true or 1, will return optional holidays from Alberta and BC.
    :type optional: str

    """
    return web.Response(status=200)
