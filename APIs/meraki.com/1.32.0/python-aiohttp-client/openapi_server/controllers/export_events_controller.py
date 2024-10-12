from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_export_event_request import CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest
from openapi_server import util


async def create_organization_inventory_onboarding_cloud_monitoring_export_event_4(request: web.Request, organization_id, body) -> web.Response:
    """Imports event logs related to the onboarding app into elastisearch

    Imports event logs related to the onboarding app into elastisearch

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest.from_dict(body)
    return web.Response(status=200)
