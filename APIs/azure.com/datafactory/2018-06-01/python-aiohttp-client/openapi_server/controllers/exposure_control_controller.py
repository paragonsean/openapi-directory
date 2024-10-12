from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.exposure_control_request import ExposureControlRequest
from openapi_server.models.exposure_control_response import ExposureControlResponse
from openapi_server import util


async def exposure_control_get_feature_value(request: web.Request, subscription_id, location_id, api_version, exposure_control_request) -> web.Response:
    """exposure_control_get_feature_value

    Get exposure control feature for specific location.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param location_id: The location identifier.
    :type location_id: str
    :param api_version: The API version.
    :type api_version: str
    :param exposure_control_request: The exposure control request.
    :type exposure_control_request: dict | bytes

    """
    exposure_control_request = ExposureControlRequest.from_dict(exposure_control_request)
    return web.Response(status=200)


async def exposure_control_get_feature_value_by_factory(request: web.Request, subscription_id, resource_group_name, factory_name, api_version, exposure_control_request) -> web.Response:
    """exposure_control_get_feature_value_by_factory

    Get exposure control feature for specific factory.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param api_version: The API version.
    :type api_version: str
    :param exposure_control_request: The exposure control request.
    :type exposure_control_request: dict | bytes

    """
    exposure_control_request = ExposureControlRequest.from_dict(exposure_control_request)
    return web.Response(status=200)
