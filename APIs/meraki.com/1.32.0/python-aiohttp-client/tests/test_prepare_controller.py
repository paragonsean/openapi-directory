# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_prepare201_response_inner import CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInner
from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_prepare_request import CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest


pytestmark = pytest.mark.asyncio

async def test_create_organization_inventory_onboarding_cloud_monitoring_prepare_4(client):
    """Test case for create_organization_inventory_onboarding_cloud_monitoring_prepare_4

    Initiates or updates an import session
    """
    body = openapi_server.CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/inventory/onboarding/cloudMonitoring/prepare'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

