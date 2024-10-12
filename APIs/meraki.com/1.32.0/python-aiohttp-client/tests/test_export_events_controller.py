# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_export_event_request import CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest


pytestmark = pytest.mark.asyncio

async def test_create_organization_inventory_onboarding_cloud_monitoring_export_event_4(client):
    """Test case for create_organization_inventory_onboarding_cloud_monitoring_export_event_4

    Imports event logs related to the onboarding app into elastisearch
    """
    body = openapi_server.CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/inventory/onboarding/cloudMonitoring/exportEvents'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

