from typing import List, Dict
from aiohttp import web

from openapi_server.models.billing_response_list_result import BillingResponseListResult
from openapi_server.models.capabilities_result import CapabilitiesResult
from openapi_server.models.locations_list_billing_specs_default_response import LocationsListBillingSpecsDefaultResponse
from openapi_server.models.usages_list_result import UsagesListResult
from openapi_server import util


async def locations_get_capabilities(request: web.Request, subscription_id, location, api_version) -> web.Response:
    """locations_get_capabilities

    Gets the capabilities for the specified location.

    :param subscription_id: The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: The Azure location (region) for which to make the request.
    :type location: str
    :param api_version: The HDInsight client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def locations_list_billing_specs(request: web.Request, subscription_id, location, api_version) -> web.Response:
    """locations_list_billing_specs

    Lists the billingSpecs for the specified subscription and location.

    :param subscription_id: The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: The Azure location (region) for which to make the request.
    :type location: str
    :param api_version: The HDInsight client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def locations_list_usages(request: web.Request, subscription_id, location, api_version) -> web.Response:
    """locations_list_usages

    Lists the usages for the specified location.

    :param subscription_id: The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: The Azure location (region) for which to make the request.
    :type location: str
    :param api_version: The HDInsight client API Version.
    :type api_version: str

    """
    return web.Response(status=200)
