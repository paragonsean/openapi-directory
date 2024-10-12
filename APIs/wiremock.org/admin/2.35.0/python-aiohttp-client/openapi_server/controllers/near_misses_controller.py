from typing import List, Dict
from aiohttp import web

from openapi_server.models.admin_mappings_get200_response_mappings_inner_request import AdminMappingsGet200ResponseMappingsInnerRequest
from openapi_server.models.admin_near_misses_request_post200_response import AdminNearMissesRequestPost200Response
from openapi_server.models.admin_near_misses_request_post_request import AdminNearMissesRequestPostRequest
from openapi_server import util


async def admin_near_misses_request_pattern_post(request: web.Request, body) -> web.Response:
    """Find near misses matching request pattern

    Find at most 3 near misses for closest logged requests to the specified request pattern

    :param body: 
    :type body: dict | bytes

    """
    body = AdminMappingsGet200ResponseMappingsInnerRequest.from_dict(body)
    return web.Response(status=200)


async def admin_near_misses_request_post(request: web.Request, body) -> web.Response:
    """Find near misses matching specific request

    Find at most 3 near misses for closest stub mappings to the specified request

    :param body: 
    :type body: dict | bytes

    """
    body = AdminNearMissesRequestPostRequest.from_dict(body)
    return web.Response(status=200)


async def admin_requests_unmatched_near_misses_get(request: web.Request, ) -> web.Response:
    """admin_requests_unmatched_near_misses_get

    Retrieve near-misses for all unmatched requests


    """
    return web.Response(status=200)
