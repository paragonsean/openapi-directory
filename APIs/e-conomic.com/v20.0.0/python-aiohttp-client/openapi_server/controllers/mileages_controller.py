from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.mileage_numbers_collection import MileageNumbersCollection
from openapi_server import util


async def approve_mileage_entries(request: web.Request, body=None) -> web.Response:
    """Approve a list of Mileage entries

    Use this endpoint to approve a list of Mileage entries.

    :param body: 
    :type body: dict | bytes

    """
    body = MileageNumbersCollection.from_dict(body)
    return web.Response(status=200)
