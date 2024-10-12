from typing import List, Dict
from aiohttp import web

from openapi_server.models.document_envelope import DocumentEnvelope
from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.error501 import Error501
from openapi_server.models.post_trip_parser_request200_response import PostTripParserRequest200Response
from openapi_server import util


async def post_trip_parser_request(request: web.Request, body=None) -> web.Response:
    """POST Trip Parser request

    

    :param body: 
    :type body: dict | bytes

    """
    body = DocumentEnvelope.from_dict(body)
    return web.Response(status=200)
