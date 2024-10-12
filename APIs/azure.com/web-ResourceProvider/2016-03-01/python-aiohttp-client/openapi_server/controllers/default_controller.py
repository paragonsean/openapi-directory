from typing import List, Dict
from aiohttp import web

from openapi_server.models.billing_meter_collection import BillingMeterCollection
from openapi_server.models.csm_move_resource_envelope import CsmMoveResourceEnvelope
from openapi_server.models.deployment_locations import DeploymentLocations
from openapi_server.models.geo_region_collection import GeoRegionCollection
from openapi_server.models.get_publishing_user200_response import GetPublishingUser200Response
from openapi_server.models.list_site_identifiers_assigned_to_host_name200_response import ListSiteIdentifiersAssignedToHostName200Response
from openapi_server.models.list_site_identifiers_assigned_to_host_name_request import ListSiteIdentifiersAssignedToHostNameRequest
from openapi_server.models.premier_add_on_offer_collection import PremierAddOnOfferCollection
from openapi_server.models.resource_name_availability import ResourceNameAvailability
from openapi_server.models.resource_name_availability_request import ResourceNameAvailabilityRequest
from openapi_server.models.sku_infos import SkuInfos
from openapi_server.models.source_control import SourceControl
from openapi_server.models.source_control_collection import SourceControlCollection
from openapi_server.models.validate_request import ValidateRequest
from openapi_server.models.validate_response import ValidateResponse
from openapi_server.models.vnet_parameters import VnetParameters
from openapi_server.models.vnet_validation_failure_details import VnetValidationFailureDetails
from openapi_server import util


async def billing_meters_list(request: web.Request, subscription_id, api_version, billing_location=None) -> web.Response:
    """Gets a list of meters for a given location.

    Gets a list of meters for a given location.

    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param billing_location: Azure Location of billable resource
    :type billing_location: str

    """
    return web.Response(status=200)


async def check_name_availability(request: web.Request, subscription_id, api_version, request) -> web.Response:
    """Check if a resource name is available.

    Check if a resource name is available.

    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param request: Name availability request.
    :type request: dict | bytes

    """
    request = ResourceNameAvailabilityRequest.from_dict(request)
    return web.Response(status=200)


async def get_publishing_user(request: web.Request, api_version) -> web.Response:
    """Gets publishing user

    Gets publishing user

    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def get_source_control(request: web.Request, source_control_type, api_version) -> web.Response:
    """Gets source control token

    Gets source control token

    :param source_control_type: Type of source control
    :type source_control_type: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def get_subscription_deployment_locations(request: web.Request, subscription_id, api_version) -> web.Response:
    """Gets list of available geo regions plus ministamps

    Gets list of available geo regions plus ministamps

    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def list_geo_regions(request: web.Request, subscription_id, api_version, sku=None, linux_workers_enabled=None) -> web.Response:
    """Get a list of available geographical regions.

    Get a list of available geographical regions.

    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param sku: Name of SKU used to filter the regions.
    :type sku: str
    :param linux_workers_enabled: Specify &lt;code&gt;true&lt;/code&gt; if you want to filter to only regions that support Linux workers.
    :type linux_workers_enabled: bool

    """
    return web.Response(status=200)


async def list_premier_add_on_offers(request: web.Request, subscription_id, api_version) -> web.Response:
    """List all premier add-on offers.

    List all premier add-on offers.

    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def list_site_identifiers_assigned_to_host_name(request: web.Request, subscription_id, api_version, name_identifier) -> web.Response:
    """List all apps that are assigned to a hostname.

    List all apps that are assigned to a hostname.

    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param name_identifier: Hostname information.
    :type name_identifier: dict | bytes

    """
    name_identifier = ListSiteIdentifiersAssignedToHostNameRequest.from_dict(name_identifier)
    return web.Response(status=200)


async def list_skus(request: web.Request, subscription_id, api_version) -> web.Response:
    """List all SKUs.

    List all SKUs.

    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def list_source_controls(request: web.Request, api_version) -> web.Response:
    """Gets the source controls available for Azure websites.

    Gets the source controls available for Azure websites.

    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def move(request: web.Request, resource_group_name, subscription_id, api_version, move_resource_envelope) -> web.Response:
    """Move resources between resource groups.

    Move resources between resource groups.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param move_resource_envelope: Object that represents the resource to move.
    :type move_resource_envelope: dict | bytes

    """
    move_resource_envelope = CsmMoveResourceEnvelope.from_dict(move_resource_envelope)
    return web.Response(status=200)


async def update_publishing_user(request: web.Request, api_version, user_details) -> web.Response:
    """Updates publishing user

    Updates publishing user

    :param api_version: API Version
    :type api_version: str
    :param user_details: Details of publishing user
    :type user_details: dict | bytes

    """
    user_details = GetPublishingUser200Response.from_dict(user_details)
    return web.Response(status=200)


async def update_source_control(request: web.Request, source_control_type, api_version, request_message) -> web.Response:
    """Updates source control token

    Updates source control token

    :param source_control_type: Type of source control
    :type source_control_type: str
    :param api_version: API Version
    :type api_version: str
    :param request_message: Source control token information
    :type request_message: dict | bytes

    """
    request_message = SourceControl.from_dict(request_message)
    return web.Response(status=200)


async def validate(request: web.Request, resource_group_name, subscription_id, api_version, validate_request) -> web.Response:
    """Validate if a resource can be created.

    Validate if a resource can be created.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param validate_request: Request with the resources to validate.
    :type validate_request: dict | bytes

    """
    validate_request = ValidateRequest.from_dict(validate_request)
    return web.Response(status=200)


async def validate_move(request: web.Request, resource_group_name, subscription_id, api_version, move_resource_envelope) -> web.Response:
    """Validate whether a resource can be moved.

    Validate whether a resource can be moved.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param move_resource_envelope: Object that represents the resource to move.
    :type move_resource_envelope: dict | bytes

    """
    move_resource_envelope = CsmMoveResourceEnvelope.from_dict(move_resource_envelope)
    return web.Response(status=200)


async def verify_hosting_environment_vnet(request: web.Request, subscription_id, api_version, parameters) -> web.Response:
    """Verifies if this VNET is compatible with an App Service Environment by analyzing the Network Security Group rules.

    Verifies if this VNET is compatible with an App Service Environment by analyzing the Network Security Group rules.

    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param parameters: VNET information
    :type parameters: dict | bytes

    """
    parameters = VnetParameters.from_dict(parameters)
    return web.Response(status=200)
