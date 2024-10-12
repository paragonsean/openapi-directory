from typing import List, Dict
from aiohttp import web

from openapi_server.models.address_validation_output import AddressValidationOutput
from openapi_server.models.available_sku_request import AvailableSkuRequest
from openapi_server.models.available_skus_result import AvailableSkusResult
from openapi_server.models.validate_address import ValidateAddress
from openapi_server import util


async def service_list_available_skus(request: web.Request, subscription_id, location, api_version, available_sku_request) -> web.Response:
    """service_list_available_skus

    This method provides the list of available skus for the given subscription and location.

    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param location: The location of the resource
    :type location: str
    :param api_version: The API Version
    :type api_version: str
    :param available_sku_request: Filters for showing the available skus.
    :type available_sku_request: dict | bytes

    """
    available_sku_request = AvailableSkuRequest.from_dict(available_sku_request)
    return web.Response(status=200)


async def service_validate_address(request: web.Request, subscription_id, location, api_version, validate_address) -> web.Response:
    """service_validate_address

    This method validates the customer shipping address and provide alternate addresses if any.

    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param location: The location of the resource
    :type location: str
    :param api_version: The API Version
    :type api_version: str
    :param validate_address: Shipping address of the customer.
    :type validate_address: dict | bytes

    """
    validate_address = ValidateAddress.from_dict(validate_address)
    return web.Response(status=200)
