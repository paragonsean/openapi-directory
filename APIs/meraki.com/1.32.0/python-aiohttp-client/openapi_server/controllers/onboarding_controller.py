from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_export_event_request import CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest
from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_import201_response_inner import CreateOrganizationInventoryOnboardingCloudMonitoringImport201ResponseInner
from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_import_request import CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest
from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_prepare201_response_inner import CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInner
from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_prepare_request import CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest
from openapi_server.models.get_network200_response import GetNetwork200Response
from openapi_server.models.get_organization_inventory_onboarding_cloud_monitoring_imports200_response_inner import GetOrganizationInventoryOnboardingCloudMonitoringImports200ResponseInner
from openapi_server.models.update_organization_camera_onboarding_statuses_request import UpdateOrganizationCameraOnboardingStatusesRequest
from openapi_server import util


async def create_organization_inventory_onboarding_cloud_monitoring_export_event_2(request: web.Request, organization_id, body) -> web.Response:
    """Imports event logs related to the onboarding app into elastisearch

    Imports event logs related to the onboarding app into elastisearch

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_inventory_onboarding_cloud_monitoring_import_2(request: web.Request, organization_id, body) -> web.Response:
    """Commits the import operation to complete the onboarding of a device into Dashboard for monitoring.

    Commits the import operation to complete the onboarding of a device into Dashboard for monitoring.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_inventory_onboarding_cloud_monitoring_prepare_2(request: web.Request, organization_id, body) -> web.Response:
    """Initiates or updates an import session

    Initiates or updates an import session. An import ID will be generated and used when you are ready to commit the import.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest.from_dict(body)
    return web.Response(status=200)


async def get_organization_camera_onboarding_statuses_1(request: web.Request, organization_id, serials=None, network_ids=None) -> web.Response:
    """Fetch onboarding status of cameras

    Fetch onboarding status of cameras

    :param organization_id: 
    :type organization_id: str
    :param serials: A list of serial numbers. The returned cameras will be filtered to only include these serials.
    :type serials: List[str]
    :param network_ids: A list of network IDs. The returned cameras will be filtered to only include these networks.
    :type network_ids: List[str]

    """
    return web.Response(status=200)


async def get_organization_inventory_onboarding_cloud_monitoring_imports_2(request: web.Request, organization_id, import_ids) -> web.Response:
    """Check the status of a committed Import operation

    Check the status of a committed Import operation

    :param organization_id: 
    :type organization_id: str
    :param import_ids: import ids from an imports
    :type import_ids: List[str]

    """
    return web.Response(status=200)


async def get_organization_inventory_onboarding_cloud_monitoring_networks_2(request: web.Request, organization_id, device_type, per_page=None, starting_after=None, ending_before=None) -> web.Response:
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


async def update_organization_camera_onboarding_statuses_1(request: web.Request, organization_id, body=None) -> web.Response:
    """Notify that credential handoff to camera has completed

    Notify that credential handoff to camera has completed

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationCameraOnboardingStatusesRequest.from_dict(body)
    return web.Response(status=200)
