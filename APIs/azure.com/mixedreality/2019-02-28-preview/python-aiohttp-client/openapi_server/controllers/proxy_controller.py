from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_name_availability_request import CheckNameAvailabilityRequest
from openapi_server.models.check_name_availability_response import CheckNameAvailabilityResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.operation_list import OperationList
from openapi_server.models.spatial_anchors_account_list import SpatialAnchorsAccountList
from openapi_server import util


async def check_name_availability_local(request: web.Request, subscription_id, location, api_version, check_name_availability) -> web.Response:
    """check_name_availability_local

    Check Name Availability for global uniqueness

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param location: The location in which uniqueness will be verified.
    :type location: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param check_name_availability: Check Name Availability Request.
    :type check_name_availability: dict | bytes

    """
    check_name_availability = CheckNameAvailabilityRequest.from_dict(check_name_availability)
    return web.Response(status=200)


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    Exposing Available Operations

    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def spatial_anchors_accounts_list_by_subscription_0(request: web.Request, subscription_id, api_version) -> web.Response:
    """spatial_anchors_accounts_list_by_subscription_0

    List Spatial Anchors Accounts by Subscription

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)
