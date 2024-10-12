from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_entitlements_request import GetEntitlementsRequest
from openapi_server.models.get_entitlements_result import GetEntitlementsResult
from openapi_server.models.internal_service_error_exception import InternalServiceErrorException
from openapi_server.models.invalid_parameter_exception import InvalidParameterException
from openapi_server.models.throttling_exception import ThrottlingException
from openapi_server import util


async def get_entitlements(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_entitlements

    GetEntitlements retrieves entitlement values for a given product. The results can be filtered based on customer identifier or product dimensions.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetEntitlementsRequest.from_dict(body)
    return web.Response(status=200)
