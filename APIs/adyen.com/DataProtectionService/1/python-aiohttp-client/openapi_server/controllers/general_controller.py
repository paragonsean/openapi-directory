from typing import List, Dict
from aiohttp import web

from openapi_server.models.service_error import ServiceError
from openapi_server.models.subject_erasure_by_psp_reference_request import SubjectErasureByPspReferenceRequest
from openapi_server.models.subject_erasure_response import SubjectErasureResponse
from openapi_server import util


async def post_request_subject_erasure(request: web.Request, body=None) -> web.Response:
    """Submit a Subject Erasure Request.

    Sends the PSP reference containing the shopper data that should be deleted.

    :param body: 
    :type body: dict | bytes

    """
    body = SubjectErasureByPspReferenceRequest.from_dict(body)
    return web.Response(status=200)
