# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_firmware_upgrades_staged_event_request import CreateNetworkFirmwareUpgradesStagedEventRequest
from openapi_server.models.get_network_events200_response import GetNetworkEvents200Response
from openapi_server.models.get_network_events_event_types200_response_inner import GetNetworkEventsEventTypes200ResponseInner
from openapi_server.models.get_network_firmware_upgrades_staged_events200_response import GetNetworkFirmwareUpgradesStagedEvents200Response
from openapi_server.models.rollbacks_network_firmware_upgrades_staged_events_request import RollbacksNetworkFirmwareUpgradesStagedEventsRequest
from openapi_server.models.update_network_firmware_upgrades_staged_events_request import UpdateNetworkFirmwareUpgradesStagedEventsRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_firmware_upgrades_staged_event_3(client):
    """Test case for create_network_firmware_upgrades_staged_event_3

    Create a Staged Upgrade Event for a network
    """
    body = openapi_server.CreateNetworkFirmwareUpgradesStagedEventRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/events'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_defer_network_firmware_upgrades_staged_events_3(client):
    """Test case for defer_network_firmware_upgrades_staged_events_3

    Postpone by 1 week all pending staged upgrade stages for a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/events/defer'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_client_security_events_3(client):
    """Test case for get_network_appliance_client_security_events_3

    List the security events for a client
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('sortOrder', 'sort_order_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/clients/{client_id}/security/events'.format(network_id='network_id_example', client_id='client_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_security_events_2(client):
    """Test case for get_network_appliance_security_events_2

    List the security events for a network
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('sortOrder', 'sort_order_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/security/events'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_events_1(client):
    """Test case for get_network_events_1

    List the events for the network
    """
    params = [('productType', 'product_type_example'),
                    ('includedEventTypes', ['included_event_types_example']),
                    ('excludedEventTypes', ['excluded_event_types_example']),
                    ('deviceMac', 'device_mac_example'),
                    ('deviceSerial', 'device_serial_example'),
                    ('deviceName', 'device_name_example'),
                    ('clientIp', 'client_ip_example'),
                    ('clientMac', 'client_mac_example'),
                    ('clientName', 'client_name_example'),
                    ('smDeviceMac', 'sm_device_mac_example'),
                    ('smDeviceName', 'sm_device_name_example'),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/events'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_events_event_types_1(client):
    """Test case for get_network_events_event_types_1

    List the event type to human-readable description
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/events/eventTypes'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_firmware_upgrades_staged_events_3(client):
    """Test case for get_network_firmware_upgrades_staged_events_3

    Get the Staged Upgrade Event from a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/events'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_appliance_security_events_2(client):
    """Test case for get_organization_appliance_security_events_2

    List the security events for an organization
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('sortOrder', 'sort_order_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/appliance/security/events'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rollbacks_network_firmware_upgrades_staged_events_3(client):
    """Test case for rollbacks_network_firmware_upgrades_staged_events_3

    Rollback a Staged Upgrade Event for a network
    """
    body = openapi_server.RollbacksNetworkFirmwareUpgradesStagedEventsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/events/rollbacks'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_firmware_upgrades_staged_events_3(client):
    """Test case for update_network_firmware_upgrades_staged_events_3

    Update the Staged Upgrade Event for a network
    """
    body = openapi_server.UpdateNetworkFirmwareUpgradesStagedEventsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/events'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

