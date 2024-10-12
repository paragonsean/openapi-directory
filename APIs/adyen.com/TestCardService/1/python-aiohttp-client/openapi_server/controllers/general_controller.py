from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_test_card_ranges_request import CreateTestCardRangesRequest
from openapi_server.models.create_test_card_ranges_result import CreateTestCardRangesResult
from openapi_server.models.service_error import ServiceError
from openapi_server import util


async def post_create_test_card_ranges(request: web.Request, body=None) -> web.Response:
    """Creates one or more test card ranges.

    Creates one or more test card ranges.

    :param body: 
    :type body: dict | bytes

    """
    body = CreateTestCardRangesRequest.from_dict(body)
    return web.Response(status=200)
