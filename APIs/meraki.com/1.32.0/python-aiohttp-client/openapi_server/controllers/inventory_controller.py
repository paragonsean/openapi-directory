from typing import List, Dict
from aiohttp import web

from openapi_server.models.claim_into_organization_inventory_request import ClaimIntoOrganizationInventoryRequest
from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_export_event_request import CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest
from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_import201_response_inner import CreateOrganizationInventoryOnboardingCloudMonitoringImport201ResponseInner
from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_import_request import CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest
from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_prepare201_response_inner import CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInner
from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_prepare_request import CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest
from openapi_server.models.get_network200_response import GetNetwork200Response
from openapi_server.models.get_organization_inventory_devices200_response_inner import GetOrganizationInventoryDevices200ResponseInner
from openapi_server.models.get_organization_inventory_onboarding_cloud_monitoring_imports200_response_inner import GetOrganizationInventoryOnboardingCloudMonitoringImports200ResponseInner
from openapi_server.models.release_from_organization_inventory_request import ReleaseFromOrganizationInventoryRequest
from openapi_server import util


async def claim_into_organization_inventory_1(request: web.Request, organization_id, body=None) -> web.Response:
    """Claim a list of devices, licenses, and/or orders into an organization inventory

    Claim a list of devices, licenses, and/or orders into an organization inventory. When claiming by order, all devices and licenses in the order will be claimed; licenses will be added to the organization and devices will be placed in the organization&#39;s inventory. Use /organizations/{organizationId}/inventory/release to release devices from an organization.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ClaimIntoOrganizationInventoryRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_inventory_onboarding_cloud_monitoring_export_event_1(request: web.Request, organization_id, body) -> web.Response:
    """Imports event logs related to the onboarding app into elastisearch

    Imports event logs related to the onboarding app into elastisearch

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_inventory_onboarding_cloud_monitoring_import_1(request: web.Request, organization_id, body) -> web.Response:
    """Commits the import operation to complete the onboarding of a device into Dashboard for monitoring.

    Commits the import operation to complete the onboarding of a device into Dashboard for monitoring.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_inventory_onboarding_cloud_monitoring_prepare_1(request: web.Request, organization_id, body) -> web.Response:
    """Initiates or updates an import session

    Initiates or updates an import session. An import ID will be generated and used when you are ready to commit the import.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest.from_dict(body)
    return web.Response(status=200)


async def get_organization_inventory_device_1(request: web.Request, organization_id, serial) -> web.Response:
    """Return a single device from the inventory of an organization

    Return a single device from the inventory of an organization

    :param organization_id: 
    :type organization_id: str
    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_organization_inventory_devices_1(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, used_state=None, search=None, macs=None, network_ids=None, serials=None, models=None, order_numbers=None, tags=None, tags_filter_type=None, product_types=None) -> web.Response:
    """Return the device inventory for an organization

    Return the device inventory for an organization

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param used_state: Filter results by used or unused inventory. Accepted values are &#39;used&#39; or &#39;unused&#39;.
    :type used_state: str
    :param search: Search for devices in inventory based on serial number, mac address, or model.
    :type search: str
    :param macs: Search for devices in inventory based on mac addresses.
    :type macs: List[str]
    :param network_ids: Search for devices in inventory based on network ids.
    :type network_ids: List[str]
    :param serials: Search for devices in inventory based on serials.
    :type serials: List[str]
    :param models: Search for devices in inventory based on model.
    :type models: List[str]
    :param order_numbers: Search for devices in inventory based on order numbers.
    :type order_numbers: List[str]
    :param tags: Filter devices by tags. The filtering is case-sensitive. If tags are included, &#39;tagsFilterType&#39; should also be included (see below).
    :type tags: List[str]
    :param tags_filter_type: To use with &#39;tags&#39; parameter, to filter devices which contain ANY or ALL given tags. Accepted values are &#39;withAnyTags&#39; or &#39;withAllTags&#39;, default is &#39;withAnyTags&#39;.
    :type tags_filter_type: str
    :param product_types: Filter devices by product type. Accepted values are appliance, camera, cellularGateway, sensor, switch, systemsManager, and wireless.
    :type product_types: List[str]

    """
    return web.Response(status=200)


async def get_organization_inventory_onboarding_cloud_monitoring_imports_1(request: web.Request, organization_id, import_ids) -> web.Response:
    """Check the status of a committed Import operation

    Check the status of a committed Import operation

    :param organization_id: 
    :type organization_id: str
    :param import_ids: import ids from an imports
    :type import_ids: List[str]

    """
    return web.Response(status=200)


async def get_organization_inventory_onboarding_cloud_monitoring_networks_1(request: web.Request, organization_id, device_type, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Returns list of networks eligible for adding cloud monitored device

    Returns list of networks eligible for adding cloud monitored device

    :param organization_id: 
    :type organization_id: str
    :param device_type: Device Type switch or wireless controller
    :type device_type: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def release_from_organization_inventory_1(request: web.Request, organization_id, body=None) -> web.Response:
    """Release a list of claimed devices from an organization.

    Release a list of claimed devices from an organization.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReleaseFromOrganizationInventoryRequest.from_dict(body)
    return web.Response(status=200)
