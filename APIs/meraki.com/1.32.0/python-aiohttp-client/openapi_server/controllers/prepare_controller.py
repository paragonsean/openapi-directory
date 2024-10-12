from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_prepare201_response_inner import CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInner
from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_prepare_request import CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest
from openapi_server import util


async def create_organization_inventory_onboarding_cloud_monitoring_prepare_4(request: web.Request, organization_id, body) -> web.Response:
    """Initiates or updates an import session

    Initiates or updates an import session. An import ID will be generated and used when you are ready to commit the import.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest.from_dict(body)
    return web.Response(status=200)
