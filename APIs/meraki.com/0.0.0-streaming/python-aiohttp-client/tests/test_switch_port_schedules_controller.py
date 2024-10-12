# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_switch_port_schedule_request import CreateNetworkSwitchPortScheduleRequest
from openapi_server.models.update_network_switch_port_schedule_request import UpdateNetworkSwitchPortScheduleRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_switch_port_schedule(client):
    """Test case for create_network_switch_port_schedule

    Add a switch port schedule
    """
    body = openapi_server.CreateNetworkSwitchPortScheduleRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v0/networks/{network_id}/switch/portSchedules'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_switch_port_schedule(client):
    """Test case for delete_network_switch_port_schedule

    Delete a switch port schedule
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v0/networks/{network_id}/switch/portSchedules/{port_schedule_id}'.format(network_id='network_id_example', port_schedule_id='port_schedule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_port_schedules(client):
    """Test case for get_network_switch_port_schedules

    List switch port schedules
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/switch/portSchedules'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_port_schedule(client):
    """Test case for update_network_switch_port_schedule

    Update a switch port schedule
    """
    body = openapi_server.UpdateNetworkSwitchPortScheduleRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/networks/{network_id}/switch/portSchedules/{port_schedule_id}'.format(network_id='network_id_example', port_schedule_id='port_schedule_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

