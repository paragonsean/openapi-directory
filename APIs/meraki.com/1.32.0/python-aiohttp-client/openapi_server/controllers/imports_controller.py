from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_import201_response_inner import CreateOrganizationInventoryOnboardingCloudMonitoringImport201ResponseInner
from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_import_request import CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest
from openapi_server.models.get_organization_inventory_onboarding_cloud_monitoring_imports200_response_inner import GetOrganizationInventoryOnboardingCloudMonitoringImports200ResponseInner
from openapi_server import util


async def create_organization_inventory_onboarding_cloud_monitoring_import_4(request: web.Request, organization_id, body) -> web.Response:
    """Commits the import operation to complete the onboarding of a device into Dashboard for monitoring.

    Commits the import operation to complete the onboarding of a device into Dashboard for monitoring.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest.from_dict(body)
    return web.Response(status=200)


async def get_organization_inventory_onboarding_cloud_monitoring_imports_4(request: web.Request, organization_id, import_ids) -> web.Response:
    """Check the status of a committed Import operation

    Check the status of a committed Import operation

    :param organization_id: 
    :type organization_id: str
    :param import_ids: import ids from an imports
    :type import_ids: List[str]

    """
    return web.Response(status=200)
