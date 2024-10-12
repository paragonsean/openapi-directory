# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_firmware_upgrades_staged_event_request import CreateNetworkFirmwareUpgradesStagedEventRequest
from openapi_server.models.create_network_firmware_upgrades_staged_group_request import CreateNetworkFirmwareUpgradesStagedGroupRequest
from openapi_server.models.get_network_firmware_upgrades_staged_events200_response import GetNetworkFirmwareUpgradesStagedEvents200Response
from openapi_server.models.get_network_firmware_upgrades_staged_groups200_response_inner import GetNetworkFirmwareUpgradesStagedGroups200ResponseInner
from openapi_server.models.get_network_firmware_upgrades_staged_stages200_response_inner import GetNetworkFirmwareUpgradesStagedStages200ResponseInner
from openapi_server.models.rollbacks_network_firmware_upgrades_staged_events_request import RollbacksNetworkFirmwareUpgradesStagedEventsRequest
from openapi_server.models.update_network_firmware_upgrades_staged_events_request import UpdateNetworkFirmwareUpgradesStagedEventsRequest
from openapi_server.models.update_network_firmware_upgrades_staged_stages_request import UpdateNetworkFirmwareUpgradesStagedStagesRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_firmware_upgrades_staged_event_2(client):
    """Test case for create_network_firmware_upgrades_staged_event_2

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

async def test_create_network_firmware_upgrades_staged_group_2(client):
    """Test case for create_network_firmware_upgrades_staged_group_2

    Create a Staged Upgrade Group for a network
    """
    body = openapi_server.CreateNetworkFirmwareUpgradesStagedGroupRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/groups'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_defer_network_firmware_upgrades_staged_events_2(client):
    """Test case for defer_network_firmware_upgrades_staged_events_2

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

async def test_delete_network_firmware_upgrades_staged_group_2(client):
    """Test case for delete_network_firmware_upgrades_staged_group_2

    Delete a Staged Upgrade Group
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/groups/{group_id}'.format(network_id='network_id_example', group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_firmware_upgrades_staged_events_2(client):
    """Test case for get_network_firmware_upgrades_staged_events_2

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

async def test_get_network_firmware_upgrades_staged_group_2(client):
    """Test case for get_network_firmware_upgrades_staged_group_2

    Get a Staged Upgrade Group from a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/groups/{group_id}'.format(network_id='network_id_example', group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_firmware_upgrades_staged_groups_2(client):
    """Test case for get_network_firmware_upgrades_staged_groups_2

    List of Staged Upgrade Groups in a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/groups'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_firmware_upgrades_staged_stages_2(client):
    """Test case for get_network_firmware_upgrades_staged_stages_2

    Order of Staged Upgrade Groups in a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/stages'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rollbacks_network_firmware_upgrades_staged_events_2(client):
    """Test case for rollbacks_network_firmware_upgrades_staged_events_2

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

async def test_update_network_firmware_upgrades_staged_events_2(client):
    """Test case for update_network_firmware_upgrades_staged_events_2

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


pytestmark = pytest.mark.asyncio

async def test_update_network_firmware_upgrades_staged_group_2(client):
    """Test case for update_network_firmware_upgrades_staged_group_2

    Update a Staged Upgrade Group for a network
    """
    body = openapi_server.CreateNetworkFirmwareUpgradesStagedGroupRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/groups/{group_id}'.format(network_id='network_id_example', group_id='group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_firmware_upgrades_staged_stages_2(client):
    """Test case for update_network_firmware_upgrades_staged_stages_2

    Assign Staged Upgrade Group order in the sequence.
    """
    body = openapi_server.UpdateNetworkFirmwareUpgradesStagedStagesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/stages'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

