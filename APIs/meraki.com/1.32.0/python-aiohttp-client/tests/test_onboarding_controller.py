# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_export_event_request import CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest
from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_import201_response_inner import CreateOrganizationInventoryOnboardingCloudMonitoringImport201ResponseInner
from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_import_request import CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest
from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_prepare201_response_inner import CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInner
from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_prepare_request import CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest
from openapi_server.models.get_network200_response import GetNetwork200Response
from openapi_server.models.get_organization_inventory_onboarding_cloud_monitoring_imports200_response_inner import GetOrganizationInventoryOnboardingCloudMonitoringImports200ResponseInner
from openapi_server.models.update_organization_camera_onboarding_statuses_request import UpdateOrganizationCameraOnboardingStatusesRequest


pytestmark = pytest.mark.asyncio

async def test_create_organization_inventory_onboarding_cloud_monitoring_export_event_2(client):
    """Test case for create_organization_inventory_onboarding_cloud_monitoring_export_event_2

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


pytestmark = pytest.mark.asyncio

async def test_create_organization_inventory_onboarding_cloud_monitoring_import_2(client):
    """Test case for create_organization_inventory_onboarding_cloud_monitoring_import_2

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

async def test_create_organization_inventory_onboarding_cloud_monitoring_prepare_2(client):
    """Test case for create_organization_inventory_onboarding_cloud_monitoring_prepare_2

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


pytestmark = pytest.mark.asyncio

async def test_get_organization_camera_onboarding_statuses_1(client):
    """Test case for get_organization_camera_onboarding_statuses_1

    Fetch onboarding status of cameras
    """
    params = [('serials', ['serials_example']),
                    ('networkIds', ['network_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/camera/onboarding/statuses'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_inventory_onboarding_cloud_monitoring_imports_2(client):
    """Test case for get_organization_inventory_onboarding_cloud_monitoring_imports_2

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


pytestmark = pytest.mark.asyncio

async def test_get_organization_inventory_onboarding_cloud_monitoring_networks_2(client):
    """Test case for get_organization_inventory_onboarding_cloud_monitoring_networks_2

    Returns list of networks eligible for adding cloud monitored device
    """
    params = [('deviceType', 'device_type_example'),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/inventory/onboarding/cloudMonitoring/networks'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_camera_onboarding_statuses_1(client):
    """Test case for update_organization_camera_onboarding_statuses_1

    Notify that credential handoff to camera has completed
    """
    body = openapi_server.UpdateOrganizationCameraOnboardingStatusesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/camera/onboarding/statuses'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

