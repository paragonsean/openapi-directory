from typing import List, Dict
from aiohttp import web

from openapi_server.models.admin_mappings_find_by_metadata_post_request import AdminMappingsFindByMetadataPostRequest
from openapi_server.models.admin_mappings_get200_response_mappings_inner_request import AdminMappingsGet200ResponseMappingsInnerRequest
from openapi_server.models.admin_requests_count_post200_response import AdminRequestsCountPost200Response
from openapi_server import util


async def admin_requests_count_post(request: web.Request, body) -> web.Response:
    """Count requests by criteria

    Count requests logged in the journal matching the specified criteria

    :param body: 
    :type body: dict | bytes

    """
    body = AdminMappingsGet200ResponseMappingsInnerRequest.from_dict(body)
    return web.Response(status=200)


async def admin_requests_delete(request: web.Request, ) -> web.Response:
    """Delete all requests in journal

    


    """
    return web.Response(status=200)


async def admin_requests_find_post(request: web.Request, body) -> web.Response:
    """Find requests by criteria

    Retrieve details of requests logged in the journal matching the specified criteria

    :param body: 
    :type body: dict | bytes

    """
    body = AdminMappingsGet200ResponseMappingsInnerRequest.from_dict(body)
    return web.Response(status=200)


async def admin_requests_get(request: web.Request, limit=None, since=None) -> web.Response:
    """Get all requests in journal

    

    :param limit: The maximum number of results to return
    :type limit: str
    :param since: Only return logged requests after this date
    :type since: str

    """
    return web.Response(status=200)


async def admin_requests_remove_by_metadata_post(request: web.Request, body=None) -> web.Response:
    """Delete requests mappings matching metadata

    

    :param body: 
    :type body: dict | bytes

    """
    body = AdminMappingsFindByMetadataPostRequest.from_dict(body)
    return web.Response(status=200)


async def admin_requests_remove_post(request: web.Request, body) -> web.Response:
    """Remove requests by criteria

    Removed requests logged in the journal matching the specified criteria

    :param body: 
    :type body: dict | bytes

    """
    body = AdminMappingsGet200ResponseMappingsInnerRequest.from_dict(body)
    return web.Response(status=200)


async def admin_requests_request_id_delete(request: web.Request, request_id) -> web.Response:
    """Delete request by ID

    

    :param request_id: The UUID of the logged request
    :type request_id: str

    """
    return web.Response(status=200)


async def admin_requests_request_id_get(request: web.Request, request_id) -> web.Response:
    """Get request by ID

    

    :param request_id: The UUID of the logged request
    :type request_id: str

    """
    return web.Response(status=200)


async def admin_requests_reset_post(request: web.Request, ) -> web.Response:
    """Empty the request journal

    


    """
    return web.Response(status=200)


async def admin_requests_unmatched_get(request: web.Request, ) -> web.Response:
    """Find unmatched requests

    Get details of logged requests that weren&#39;t matched by any stub mapping


    """
    return web.Response(status=200)
