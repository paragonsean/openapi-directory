from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_verification_request import AddVerificationRequest
from openapi_server.models.add_verification_response import AddVerificationResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_all_verifications_response import GetAllVerificationsResponse
from openapi_server.models.verify_request import VerifyRequest
from openapi_server import util


async def add_verification(request: web.Request, body) -> web.Response:
    """Start verification process for external email address or sms number

    

    :param body: Key body
    :type body: dict | bytes

    """
    body = AddVerificationRequest.from_dict(body)
    return web.Response(status=200)


async def get_all_verifications(request: web.Request, ) -> web.Response:
    """Get all verificats for the user

    


    """
    return web.Response(status=200)


async def verify(request: web.Request, verification, body) -> web.Response:
    """Verify an email address or sms number with a code

    

    :param verification: ID of the verification entry
    :type verification: str
    :param body: Verify action body
    :type body: dict | bytes

    """
    body = VerifyRequest.from_dict(body)
    return web.Response(status=200)
