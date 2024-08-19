from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_management_service_check_name_availability_default_response import ApiManagementServiceCheckNameAvailabilityDefaultResponse
from openapi_server.models.resource_sku_results import ResourceSkuResults
from openapi_server import util


async def api_management_service_skus_list_available_service_skus(request: web.Request, resource_group_name, service_name, api_version, subscription_id) -> web.Response:
    """Gets available SKUs for API Management service

    Gets all available SKU for a given API Management service

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
