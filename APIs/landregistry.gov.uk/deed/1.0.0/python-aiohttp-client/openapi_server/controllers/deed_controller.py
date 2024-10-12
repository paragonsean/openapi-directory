from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.operative_deed import OperativeDeed
from openapi_server import util


async def deed_deed_reference_get(request: web.Request, deed_reference) -> web.Response:
    """Deed

    The Deed endpoint returns details of a specific deed based on the unique deed reference. The response includes the Title Number, Property information, Borrower(s) information and deed information. 

    :param deed_reference: Unique reference of the deed.
    :type deed_reference: str

    """
    return web.Response(status=200)
