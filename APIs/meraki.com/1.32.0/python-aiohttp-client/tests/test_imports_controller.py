# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_import201_response_inner import CreateOrganizationInventoryOnboardingCloudMonitoringImport201ResponseInner
from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_import_request import CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest
from openapi_server.models.get_organization_inventory_onboarding_cloud_monitoring_imports200_response_inner import GetOrganizationInventoryOnboardingCloudMonitoringImports200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_create_organization_inventory_onboarding_cloud_monitoring_import_4(client):
    """Test case for create_organization_inventory_onboarding_cloud_monitoring_import_4

    Commits the import operation to complete the onboarding of a device into Dashboard for monitoring.
    """
    body = openapi_server.CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/inventory/onboarding/cloudMonitoring/imports'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_inventory_onboarding_cloud_monitoring_imports_4(client):
    """Test case for get_organization_inventory_onboarding_cloud_monitoring_imports_4

    Check the status of a committed Import operation
    """
    params = [('importIds', ['import_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/inventory/onboarding/cloudMonitoring/imports'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

