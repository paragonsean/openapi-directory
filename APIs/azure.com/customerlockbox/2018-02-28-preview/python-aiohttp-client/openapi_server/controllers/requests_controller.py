from typing import List, Dict
from aiohttp import web

from openapi_server.models.approval import Approval
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.lockbox_request_response import LockboxRequestResponse
from openapi_server.models.request_list_result import RequestListResult
from openapi_server import util


async def requests_get(request: web.Request, request_id, subscription_id, api_version) -> web.Response:
    """requests_get

    Get Customer Lockbox request

    :param request_id: The Lockbox request ID.
    :type request_id: str
    :param subscription_id: The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    :type subscription_id: str
    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str

    """
    return web.Response(status=200)


async def requests_list(request: web.Request, subscription_id, filter=None) -> web.Response:
    """requests_list

    Lists all of the Lockbox requests in the given subscription.

    :param subscription_id: The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    :type subscription_id: str
    :param filter: The $filter OData query parameter. Only filter by request status is supported, e.g $filter&#x3D;properties/status eq &#39;Pending&#39;
    :type filter: str

    """
    return web.Response(status=200)


async def requests_update_status(request: web.Request, subscription_id, request_id, api_version, approval) -> web.Response:
    """requests_update_status

    Update Customer Lockbox request approval status API

    :param subscription_id: The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    :type subscription_id: str
    :param request_id: The Lockbox request ID.
    :type request_id: str
    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str
    :param approval: The approval object to update request status.
    :type approval: dict | bytes

    """
    approval = Approval.from_dict(approval)
    return web.Response(status=200)
