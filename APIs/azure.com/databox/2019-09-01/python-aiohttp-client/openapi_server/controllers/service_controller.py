from typing import List, Dict
from aiohttp import web

from openapi_server.models.address_validation_output import AddressValidationOutput
from openapi_server.models.available_sku_request import AvailableSkuRequest
from openapi_server.models.available_skus_result import AvailableSkusResult
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.region_configuration_request import RegionConfigurationRequest
from openapi_server.models.region_configuration_response import RegionConfigurationResponse
from openapi_server.models.validate_address import ValidateAddress
from openapi_server.models.validation_request import ValidationRequest
from openapi_server.models.validation_response import ValidationResponse
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


async def service_list_available_skus_by_resource_group(request: web.Request, subscription_id, resource_group_name, location, api_version, available_sku_request) -> web.Response:
    """service_list_available_skus_by_resource_group

    This method provides the list of available skus for the given subscription, resource group and location.

    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param location: The location of the resource
    :type location: str
    :param api_version: The API Version
    :type api_version: str
    :param available_sku_request: Filters for showing the available skus.
    :type available_sku_request: dict | bytes

    """
    available_sku_request = AvailableSkuRequest.from_dict(available_sku_request)
    return web.Response(status=200)


async def service_region_configuration(request: web.Request, subscription_id, location, api_version, region_configuration_request) -> web.Response:
    """service_region_configuration

    This API provides configuration details specific to given region/location.

    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param location: The location of the resource
    :type location: str
    :param api_version: The API Version
    :type api_version: str
    :param region_configuration_request: Request body to get the configuration for the region.
    :type region_configuration_request: dict | bytes

    """
    region_configuration_request = RegionConfigurationRequest.from_dict(region_configuration_request)
    return web.Response(status=200)


async def service_validate_address(request: web.Request, subscription_id, location, api_version, validate_address) -> web.Response:
    """service_validate_address

    [DEPRECATED NOTICE: This operation will soon be removed] This method validates the customer shipping address and provide alternate addresses if any.

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


async def service_validate_inputs(request: web.Request, subscription_id, location, api_version, validation_request) -> web.Response:
    """service_validate_inputs

    This method does all necessary pre-job creation validation under subscription.

    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param location: The location of the resource
    :type location: str
    :param api_version: The API Version
    :type api_version: str
    :param validation_request: Inputs of the customer.
    :type validation_request: dict | bytes

    """
    validation_request = ValidationRequest.from_dict(validation_request)
    return web.Response(status=200)


async def service_validate_inputs_by_resource_group(request: web.Request, subscription_id, resource_group_name, location, api_version, validation_request) -> web.Response:
    """service_validate_inputs_by_resource_group

    This method does all necessary pre-job creation validation under resource group.

    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param location: The location of the resource
    :type location: str
    :param api_version: The API Version
    :type api_version: str
    :param validation_request: Inputs of the customer.
    :type validation_request: dict | bytes

    """
    validation_request = ValidationRequest.from_dict(validation_request)
    return web.Response(status=200)
