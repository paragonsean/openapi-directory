# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_claim_into_organization_inventory_1(client):
    """Test case for claim_into_organization_inventory_1

    Claim a list of devices, licenses, and/or orders into an organization inventory
    """
    body = openapi_server.ClaimIntoOrganizationInventoryRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/inventory/claim'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_organization_inventory_onboarding_cloud_monitoring_export_event_1(client):
    """Test case for create_organization_inventory_onboarding_cloud_monitoring_export_event_1

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

async def test_create_organization_inventory_onboarding_cloud_monitoring_import_1(client):
    """Test case for create_organization_inventory_onboarding_cloud_monitoring_import_1

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

async def test_create_organization_inventory_onboarding_cloud_monitoring_prepare_1(client):
    """Test case for create_organization_inventory_onboarding_cloud_monitoring_prepare_1

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

async def test_get_organization_inventory_device_1(client):
    """Test case for get_organization_inventory_device_1

    Return a single device from the inventory of an organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/inventory/devices/{serial}'.format(organization_id='organization_id_example', serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_inventory_devices_1(client):
    """Test case for get_organization_inventory_devices_1

    Return the device inventory for an organization
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('usedState', 'used_state_example'),
                    ('search', 'search_example'),
                    ('macs', ['macs_example']),
                    ('networkIds', ['network_ids_example']),
                    ('serials', ['serials_example']),
                    ('models', ['models_example']),
                    ('orderNumbers', ['order_numbers_example']),
                    ('tags', ['tags_example']),
                    ('tagsFilterType', 'tags_filter_type_example'),
                    ('productTypes', ['product_types_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/inventory/devices'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_inventory_onboarding_cloud_monitoring_imports_1(client):
    """Test case for get_organization_inventory_onboarding_cloud_monitoring_imports_1

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

async def test_get_organization_inventory_onboarding_cloud_monitoring_networks_1(client):
    """Test case for get_organization_inventory_onboarding_cloud_monitoring_networks_1

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

async def test_release_from_organization_inventory_1(client):
    """Test case for release_from_organization_inventory_1

    Release a list of claimed devices from an organization.
    """
    body = openapi_server.ReleaseFromOrganizationInventoryRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/inventory/release'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

